<h1 align="center">Hi, I'm k-is-sick </h1>
<p align="center">MLOps / AI-ML · building infra by hand before trusting the managed version</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="dark_mode.svg">
    <source media="(prefers-color-scheme: light)" srcset="light_mode.svg">
    <img alt="live github stats" src="light_mode.svg">
  </picture>
</p>

<p align="center"><i>Stats above update automatically once a day via GitHub Actions — see <code>today.py</code>.</i></p>

---

### What I'm building

- **LocalAWS** — a local AWS clone (Docker + Flask + Python): Mini-S3, Mini-EC2 using Docker containers as instances with `ttyd` for browser-based console access, and Mini-IAM with AWS-style users, access keys, and JSON policy documents.
- Client AWS setups — account/IAM/MFA foundations and billing guardrails.
- Working through AWS end to end: VPC architecture, S3 → Glue → Athena ETL pipelines, Rekognition-based serverless detection apps.

---

### Projects

| Project | What it does | Stack |
|---|---|---|
| **[LocalAWS](https://github.com/k-is-sick/Local_AWS)** | Local AWS clone with Mini-S3, Mini-EC2 (Docker-as-instances w/ browser terminals), and Mini-IAM (policy-based access control) | Python, Flask, PostgreSQL, Docker |
| **AWS VPC Architecture** | Full public/private subnet setup with Flask frontend, MySQL backend, NAT Gateway, and IGW | AWS, Flask, MySQL |
| **AWS ETL Pipeline** | S3 → Glue ETL (PySpark) → Glue Crawler pipeline on a synthetic dataset with intentional data quality issues | AWS S3, Glue, PySpark |
| **Serverless Gun Detection App** | Real-time object detection app on AWS using Rekognition Custom Labels, achieving perfect F1/precision/recall | AWS Rekognition, Lambda, API Gateway, S3 |
| **ML Model Deployment (FastAPI + Docker)** | Trained model served via FastAPI, containerized end-to-end, runnable from Colab | Python, Scikit-learn, FastAPI, Docker |
| **3-Container MLOps App** | MySQL + Node.js/Express + frontend with health-check-enforced startup ordering | Docker Compose, MySQL, Node.js |
| **Credit Card Fraud Detection** | Imbalanced classification (~0.17% fraud rate) comparing raw, undersampled, and SMOTE-balanced Logistic Regression, evaluated on recall/precision/ROC-AUC | Python, Scikit-learn, SMOTE |
| **ALERT — Driver Drowsiness Detection** | Edge AI system using facial landmarks (EAR/MAR/PERCLOS) on Raspberry Pi 5 / Jetson Orin Nano — 96.4% accuracy at <5ms latency | Python, OpenCV, Edge AI |
| **Gemma Fine-Tuning for Mental Health** | Parameter-efficient fine-tuning of Google Gemma using SFTTrainer + LoRA | Hugging Face, LoRA, BitsAndBytes |

---

### Stack

<table>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" height="24" alt="c" /> C</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" height="24" alt="cpp" /> C++</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" height="24" alt="csharp" /> C#</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="24" alt="html5" /> HTML5</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="24" alt="css3" /> CSS3</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" height="24" alt="go" /> Go</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="24" alt="python" /> Python</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" height="24" alt="jupyter" /> Jupyter</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg" height="24" alt="pytorch" /> PyTorch</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" height="24" alt="pytest" /> Pytest</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" height="24" alt="aws" /> AWS</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/anaconda/anaconda-original.svg" height="24" alt="anaconda" /> Anaconda</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/android/android-original.svg" height="24" alt="android" /> Android</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/androidstudio/androidstudio-original.svg" height="24" alt="androidstudio" /> Android Studio</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg" height="24" alt="arduino" /> Arduino</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="24" alt="bash" /> Bash</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/blender/blender-original.svg" height="24" alt="blender" /> Blender</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dart/dart-original.svg" height="24" alt="dart" /> Dart</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/debian/debian-original.svg" height="24" alt="debian" /> Debian</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="24" alt="docker" /> Docker</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dot-net/dot-net-original.svg" height="24" alt="dotnet" /> .NET</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dotnetcore/dotnetcore-original.svg" height="24" alt="dotnetcore" /> .NET Core</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/filezilla/filezilla-plain.svg" height="24" alt="filezilla" /> FileZilla</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flutter/flutter-original.svg" height="24" alt="flutter" /> Flutter</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="24" alt="flask" /> Flask</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/gcc/gcc-original.svg" height="24" alt="gcc" /> GCC</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="24" alt="git" /> Git</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" height="24" alt="github" /> GitHub</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/gitlab/gitlab-original.svg" height="24" alt="gitlab" /> GitLab</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="24" alt="googlecloud" /> Google Cloud</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/intellij/intellij-original.svg" height="24" alt="intellij" /> IntelliJ</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jetbrains/jetbrains-original.svg" height="24" alt="jetbrains" /> JetBrains</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" height="24" alt="java" /> Java</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="24" alt="javascript" /> JavaScript</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kaggle/kaggle-original.svg" height="24" alt="kaggle" /> Kaggle</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg" height="24" alt="kotlin" /> Kotlin</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg" height="24" alt="kubernetes" /> Kubernetes</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="24" alt="linux" /> Linux</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/lua/lua-original.svg" height="24" alt="lua" /> Lua</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/markdown/markdown-original.svg" height="24" alt="markdown" /> Markdown</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matlab/matlab-original.svg" height="24" alt="matlab" /> MATLAB</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="24" alt="mysql" /> MySQL</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" height="24" alt="mongodb" /> MongoDB</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg" height="24" alt="nginx" /> Nginx</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" height="24" alt="nodejs" /> Node.js</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg" height="24" alt="npm" /> npm</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nuget/nuget-original.svg" height="24" alt="nuget" /> NuGet</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="24" alt="numpy" /> NumPy</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" height="24" alt="opencv" /> OpenCV</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opengl/opengl-original.svg" height="24" alt="opengl" /> OpenGL</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/oracle/oracle-original.svg" height="24" alt="oracle" /> Oracle</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="24" alt="pandas" /> Pandas</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="24" alt="postgresql" /> PostgreSQL</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pycharm/pycharm-original.svg" height="24" alt="pycharm" /> PyCharm</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/putty/putty-original.svg" height="24" alt="putty" /> PuTTY</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" height="24" alt="react" /> React</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" height="24" alt="sqlite" /> SQLite</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/swift/swift-original.svg" height="24" alt="swift" /> Swift</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="24" alt="tensorflow" /> TensorFlow</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/unix/unix-original.svg" height="24" alt="unix" /> Unix</td>
</tr>
<tr>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vim/vim-original.svg" height="24" alt="vim" /> Vim</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/visualstudio/visualstudio-plain.svg" height="24" alt="visualstudio" /> Visual Studio</td>
<td><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="24" alt="vscode" /> VS Code</td>
<td></td>
</tr>
</table>

---

<p align="center"><sub>This README's stats card is generated by a script in this repo, not a third-party badge service.</sub></p>