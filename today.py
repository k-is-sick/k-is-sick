#!/usr/bin/env python3
"""
today.py
--------
Pulls live stats from the GitHub API (repos, stars, commits, contributions,
followers, and total lines of code added/deleted) and stamps them into
templates/light_mode.svg and templates/dark_mode.svg, writing the result
to the repo root as light_mode.svg / dark_mode.svg.

Run by .github/workflows/main.yml on a daily schedule and on every push.

Env vars required:
    ACCESS_TOKEN  - a GitHub PAT (classic) with 'repo' + 'read:user' scope
    USER_NAME     - the GitHub username to report on (defaults below)
"""

import os
import re
import time
import datetime
import requests

# ----------------------------------------------------------------------------
# Config
# ----------------------------------------------------------------------------
USER_NAME = os.environ.get("USER_NAME", "k-is-sick")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "")
HEADERS = {"Authorization": f"bearer {ACCESS_TOKEN}"}
GRAPHQL_URL = "https://api.github.com/graphql"
REST_URL = "https://api.github.com"
CACHE_DIR = os.path.join(os.path.dirname(__file__), "cache")
CACHE_PATH = os.path.join(CACHE_DIR, f"{USER_NAME}.txt")

QUERY_COUNT = {
    "user_getter": 0, "follower_getter": 0, "graph_repos_stars": 0,
    "recursive_loc": 0, "graph_commits": 0, "loc_query": 0,
}


def perf_counter(func, *args):
    start = time.perf_counter()
    result = func(*args)
    return result, time.perf_counter() - start


def formatter(query_type, difference, funct_return=False, whitespace=0):
    print(f"{query_type:<23}{'':<{whitespace}}", end="")
    if difference > 1:
        print(f"{difference:.4f} s")
    else:
        print(f"{difference * 1000:.4f} ms")
    return funct_return


# ----------------------------------------------------------------------------
# GraphQL helpers
# ----------------------------------------------------------------------------
def simple_request(func_name, query, variables):
    request = requests.post(GRAPHQL_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    if request.status_code == 200:
        return request
    raise Exception(f"{func_name} failed with code {request.status_code}: {request.text[:300]}")


def user_getter(username):
    """Return the user's node ID and account creation date."""
    QUERY_COUNT["user_getter"] += 1
    query = """
    query($login: String!) {
        user(login: $login) {
            id
            createdAt
        }
    }"""
    request = simple_request(user_getter.__name__, query, {"login": username})
    data = request.json()["data"]["user"]
    return {"id": data["id"]}, data["createdAt"]


def follower_getter(username):
    QUERY_COUNT["follower_getter"] += 1
    query = """
    query($login: String!) {
        user(login: $login) {
            followers {
                totalCount
            }
        }
    }"""
    request = simple_request(follower_getter.__name__, query, {"login": username})
    return int(request.json()["data"]["user"]["followers"]["totalCount"])


def graph_commits(start_date, end_date):
    """Total commits authored by the user within a date window."""
    QUERY_COUNT["graph_commits"] += 1
    query = """
    query($start: DateTime!, $end: DateTime!, $login: String!) {
        user(login: $login) {
            contributionsCollection(from: $start, to: $end) {
                contributionCalendar {
                    totalContributions
                }
            }
        }
    }"""
    variables = {"start": start_date, "end": end_date, "login": USER_NAME}
    request = simple_request(graph_commits.__name__, query, variables)
    return int(request.json()["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"])


def total_commits(created_at):
    """Sum contributionsCollection windows year by year since account creation."""
    start = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    now = datetime.datetime.utcnow()
    total = 0
    cursor = start
    while cursor < now:
        window_end = min(cursor.replace(year=cursor.year + 1), now)
        total += graph_commits(cursor.isoformat() + "Z", window_end.isoformat() + "Z")
        cursor = window_end
    return total


def graph_repos_stars(count_type, owner_affiliation, cursor=None, add_loc=0, del_loc=0):
    """Recursively paginate the user's repos to sum either repo count or star count."""
    QUERY_COUNT["graph_repos_stars"] += 1
    query = """
    query($login: String!, $affiliations: [RepositoryAffiliation], $cursor: String) {
        user(login: $login) {
            repositories(first: 100, after: $cursor, ownerAffiliations: $affiliations) {
                totalCount
                edges {
                    node {
                        ... on Repository {
                            nameWithOwner
                            stargazers { totalCount }
                        }
                    }
                }
                pageInfo { endCursor hasNextPage }
            }
        }
    }"""
    variables = {"login": USER_NAME, "affiliations": owner_affiliation, "cursor": cursor}
    request = simple_request(graph_repos_stars.__name__, query, variables)
    repos = request.json()["data"]["user"]["repositories"]

    if count_type == "repos":
        return repos["totalCount"]
    elif count_type == "stars":
        total = sum(edge["node"]["stargazers"]["totalCount"] for edge in repos["edges"])
        if repos["pageInfo"]["hasNextPage"]:
            total += graph_repos_stars("stars", owner_affiliation, repos["pageInfo"]["endCursor"])
        return total


# ----------------------------------------------------------------------------
# Lines of code (cached per repo commit-count so unchanged repos are skipped)
# ----------------------------------------------------------------------------
def load_cache():
    if not os.path.exists(CACHE_PATH):
        return {}
    cache = {}
    with open(CACHE_PATH, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 4:
                cache[parts[0]] = {"commits": int(parts[1]), "add": int(parts[2]), "del": int(parts[3])}
    return cache


def save_cache(cache):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(CACHE_PATH, "w") as f:
        for name, v in cache.items():
            f.write(f"{name} {v['commits']} {v['add']} {v['del']}\n")


def repo_commit_count(owner, name):
    url = f"{REST_URL}/repos/{owner}/{name}/commits"
    r = requests.get(url, headers=HEADERS, params={"author": USER_NAME, "per_page": 1})
    if r.status_code != 200:
        return 0
    if "last" in r.links:
        last_url = r.links["last"]["url"]
        return int(re.search(r"page=(\d+)", last_url).group(1))
    return len(r.json())


def repo_loc(owner, name):
    """Sum additions/deletions authored by USER_NAME using the stats/contributors endpoint."""
    url = f"{REST_URL}/repos/{owner}/{name}/stats/contributors"
    for _ in range(3):  # GitHub sometimes returns 202 while it computes stats
        r = requests.get(url, headers=HEADERS)
        if r.status_code == 202:
            time.sleep(2)
            continue
        if r.status_code != 200:
            return 0, 0
        break
    add, dele = 0, 0
    for entry in r.json() if isinstance(r.json(), list) else []:
        if entry.get("author", {}).get("login", "").lower() == USER_NAME.lower():
            for week in entry.get("weeks", []):
                add += week.get("a", 0)
                dele += week.get("d", 0)
    return add, dele


def list_all_repos():
    """List name-with-owner for repos where the user is owner, collaborator, or org member."""
    query = """
    query($login: String!, $affiliations: [RepositoryAffiliation], $cursor: String) {
        user(login: $login) {
            repositories(first: 100, after: $cursor, ownerAffiliations: $affiliations, isFork: false) {
                edges { node { nameWithOwner } }
                pageInfo { endCursor hasNextPage }
            }
        }
    }"""
    affiliations = ["OWNER", "COLLABORATOR", "ORGANIZATION_MEMBER"]
    cursor, names = None, []
    while True:
        request = simple_request("list_all_repos", query, {"login": USER_NAME, "affiliations": affiliations, "cursor": cursor})
        repos = request.json()["data"]["user"]["repositories"]
        names += [e["node"]["nameWithOwner"] for e in repos["edges"]]
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    return names


def loc_query():
    """Total lines added / deleted / net across all repos, using a commit-count cache."""
    QUERY_COUNT["loc_query"] += 1
    cache = load_cache()
    total_add, total_del = 0, 0
    any_uncached = False

    for full_name in list_all_repos():
        owner, name = full_name.split("/", 1)
        commits = repo_commit_count(owner, name)
        cached = cache.get(full_name)
        if cached and cached["commits"] == commits:
            total_add += cached["add"]
            total_del += cached["del"]
            continue
        any_uncached = True
        add, dele = repo_loc(owner, name)
        cache[full_name] = {"commits": commits, "add": add, "del": dele}
        total_add += add
        total_del += dele

    save_cache(cache)
    return total_add, total_del, total_add - total_del, not any_uncached


# ----------------------------------------------------------------------------
# SVG rendering
# ----------------------------------------------------------------------------
def justify_format(number):
    return "{:,}".format(number)


def svg_overwrite(filename, age_str, commit_data, star_data, repo_data, contrib_data, follower_data, loc_data):
    template_path = os.path.join(os.path.dirname(__file__), "templates", filename)
    with open(template_path, "r", encoding="utf-8") as f:
        svg = f.read()

    replacements = {
        "{{ age_data }}": age_str,
        "{{ commit_data }}": justify_format(commit_data),
        "{{ star_data }}": justify_format(star_data),
        "{{ repo_data }}": justify_format(repo_data),
        "{{ contrib_data }}": justify_format(contrib_data),
        "{{ follower_data }}": justify_format(follower_data),
        "{{ loc_add }}": justify_format(loc_data[0]),
        "{{ loc_del }}": justify_format(loc_data[1]),
        "{{ loc_net }}": justify_format(loc_data[2]),
    }
    for placeholder, value in replacements.items():
        svg = svg.replace(placeholder, str(value))

    out_path = os.path.join(os.path.dirname(__file__), filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)


def days_since(created_at):
    start = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    delta = datetime.datetime.utcnow() - start
    years, days = divmod(delta.days, 365)
    return f"{years} yrs, {days} days"


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    if not ACCESS_TOKEN:
        raise SystemExit("ACCESS_TOKEN env var is not set. See SETUP.md.")

    print(f"Calculating stats for {USER_NAME}\n{'-' * 40}")

    user_data, user_time = perf_counter(user_getter, USER_NAME)
    OWNER_ID, created_at = user_data
    formatter("account data", user_time)

    age_str = days_since(created_at)

    commit_data, commit_time = perf_counter(total_commits, created_at)
    formatter("total commits", commit_time)

    star_data, star_time = perf_counter(graph_repos_stars, "stars", ["OWNER"])
    formatter("stars", star_time)

    repo_data, repo_time = perf_counter(graph_repos_stars, "repos", ["OWNER"])
    formatter("owned repos", repo_time)

    contrib_data, contrib_time = perf_counter(graph_repos_stars, "repos", ["OWNER", "COLLABORATOR", "ORGANIZATION_MEMBER"])
    formatter("contributed-to repos", contrib_time)

    follower_data, follower_time = perf_counter(follower_getter, USER_NAME)
    formatter("followers", follower_time)

    loc_result, loc_time = perf_counter(loc_query)
    formatter("LOC (cached)" if loc_result[3] else "LOC (no cache)", loc_time)

    svg_overwrite("dark_mode.svg", age_str, commit_data, star_data, repo_data, contrib_data, follower_data, loc_result)
    svg_overwrite("light_mode.svg", age_str, commit_data, star_data, repo_data, contrib_data, follower_data, loc_result)

    total_time = user_time + commit_time + star_time + repo_time + contrib_time + follower_time + loc_time
    print("-" * 40)
    formatter("total function time", total_time)
