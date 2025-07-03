#  CI/CD with Tekton, OpenShift & Kubernetes

[![CI Build](https://github.com/gld145/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/gld145/devops-capstone-project/actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/downloads/release/python-390/)
[![Author: guylandrydjolaud](https://img.shields.io/badge/Author-guylandrydjolaud-orange)](https://github.com/guylandrydjolaud)

---

##  Overview

This repository contains the personalized version of the IBM DevOps Capstone Project.  
It features a fully automated CI/CD pipeline using **GitHub Actions**, **Tekton**, and **OpenShift**,  
with support for local Kubernetes development using **K3D**.

---

##  Usage

>  **Do not fork this repo**  
Instead, use the green **"Use this Template"** button on GitHub.  
This creates your own copy without linking it to the original like a fork.

---

##  Development Environment

This project is designed for use in the **IBM Developer Skills Network Cloud IDE** with OpenShift.

To initialize the environment:

```bash
source bin/setup.sh
```

This will:

- Install Python 3.9
- Set it as the default version
- Modify your bash prompt
- Create and activate a Python virtual environment

You should see:

```bash
(venv) theia:project$
```

---

##  Useful Commands

### Activate the virtual environment

```bash
source ~/venv/bin/activate
```

### Reinstall Python dependencies

```bash
make install
```

### Start the PostgreSQL container

```bash
make db
docker ps   # Verify it's running
```

---

##  Project Structure

```text
├── service/                # Microservice logic (Flask)
│   ├── common/             # Logging & error handling
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── tests/                  # Unit tests
│   ├── factories.py
│   ├── test_models.py
│   └── test_routes.py
├── setup.cfg
├── Makefile
├── Dockerfile
└── ci-build.yaml           # GitHub CI pipeline
```

---

##  Data Model (Accounts)

| Field         | Type        | Optional |
|---------------|-------------|----------|
| id            | Integer     | ❌       |
| name          | String(64)  | ❌       |
| email         | String(64)  | ❌       |
| address       | String(256) | ❌       |
| phone_number  | String(32)  | ✅       |
| date_joined   | Date        | ❌       |

---

##  Your Capstone Challenge

- Implement REST APIs: `READ`, `UPDATE`, `DELETE`, `LIST`
- Follow **TDD**: write tests before coding
- Maintain **95%+ test coverage**
- Use GitHub Actions + Tekton for CI/CD
- Simulate deployment via OpenShift or K3D locally

---

##  Kubernetes + Tekton (Local Setup)

You can replicate the cloud IDE on your machine using:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [K3D (Kubernetes in Docker)](https://k3d.io/)
- [VSCode Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Local Setup Commands

```bash
make cluster        # Start K3D cluster
make tekton         # Install Tekton
make clustertasks   # Add IBM Lab ClusterTasks
```

You're now ready to test Tekton pipelines locally as in the IBM Cloud IDE.

---

##  Skills Demonstrated

- CI/CD automation with GitHub Actions & Tekton
- Local Kubernetes development using K3D
- RESTful API development with Flask
- Infrastructure as Code with Makefile
- Test Driven Development (TDD)
- Containerization with Docker & Buildah

---

##  Author

Crafted with ❤️ by [Guy Landry Djolaud](https://github.com/guylandrydjolaud)  
 guylandry.djolaud@gmail.com  
 [devoptimize.tech](https://devoptimize.tech)

---

##  License

Licensed under Apache License 2.0 – see [LICENSE](LICENSE)

---

## <h3 align="center">© IBM Corporation 2022 | Customized for educational and portfolio purposes</h3>
