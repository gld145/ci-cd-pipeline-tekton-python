# CI/CD with Tekton and OpenShift

[![CI Build](https://github.com/gld145/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/gld145/devops-capstone-project/actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/downloads/release/python-390/)
[![Author: guylandrydjolaud](https://img.shields.io/badge/Author-guylandrydjolaud-orange)](https://github.com/guylandrydjolaud)

---

##  Project Overview

This repository contains the source code for my **IBM DevOps Capstone Project**, developed as part of the  
[IBM DevOps and Software Engineering Professional Certificate](https://www.coursera.org/professional-certificates/devops-and-software-engineering).  
It demonstrates a fully automated CI/CD workflow using **GitHub Actions**, **Tekton Pipelines**, and **OpenShift**, following **TDD** principles.

---

##  Usage Instructions

This project is meant to be cloned and extended.  
>  **Do not fork** — Instead, click the `Use this Template` button on GitHub to create your own copy.

---

##  Dev Environment Setup (IBM Cloud IDE)

Use the Skills Network Labs IDE provided in the Coursera labs. Initialize the environment with:

```bash
source bin/setup.sh
```

This will:
- Install Python 3.9
- Configure your environment
- Set up and activate the virtual environment

Prompt should now look like:
```bash
(venv) theia:project$
```

---

##  Useful Commands

### Activate the Python venv
```bash
source ~/venv/bin/activate
```

### Reinstall dependencies (if needed)
```bash
make install
```

### Start PostgreSQL container
```bash
make db
```

---

##  Project Structure

```text
├── service/                # Python microservice (Flask)
│   ├── common/             # Logging and error handling
│   ├── config.py
│   ├── models.py
│   └── routes.py
├── tests/                  # Unit and CLI tests
│   ├── factories.py
│   ├── test_cli_commands.py
│   ├── test_models.py
│   └── test_routes.py
├── Dockerfile
├── Makefile
├── ci-build.yaml           # GitHub Action workflow
└── setup.cfg               # Tooling configuration
```

---

##  Data Model

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

Implement full CRUD for this microservice (READ, UPDATE, DELETE, LIST).  
-  Follow **TDD**: Write tests before code  
-  Maintain **> 95%** test coverage  
-  Use GitHub Actions for CI pipeline  
-  Simulate deployment via Tekton on OpenShift

---

##  Local Kubernetes Development (Optional)

You can simulate the IBM Cloud IDE on your machine.

### Requirements:
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [VSCode](https://code.visualstudio.com) + [Remote Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [K3D](https://k3d.io/)

### Commands:

```bash
make cluster         # Set up K3D cluster
make tekton          # Install Tekton
make clustertasks    # Load Tekton ClusterTasks
```

---

##  Author

Made with ❤️ by [Guy Landry Djolaud](https://github.com/guylandrydjolaud)  
 Contact: guylandry.djolaud@gmail.com  
 Portfolio: [gldcloud](https://devoptimize.tech)

---

##  License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

---

##  Credit

Based on the original work by [John Rofrano](https://www.coursera.org/instructor/johnrofrano),  
Senior Technical Staff Member, IBM Research.

---

## <h3 align="center">© IBM Corporation 2022. All rights reserved.</h3>
