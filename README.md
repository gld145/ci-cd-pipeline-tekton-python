#  Kubernetes & Tekton Local Development 

[![CI Build](https://github.com/gld145/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/gld145/devops-capstone-project/actions)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/downloads/release/python-390/)
[![Author: guylandrydjolaud](https://img.shields.io/badge/Author-guylandrydjolaud-orange)](https://github.com/guylandrydjolaud)

---

##  Kubernetes + Tekton Local Dev Setup

You can simulate the IBM Cloud IDE experience directly on your local machine using Kubernetes (via K3D), Docker Desktop, and VSCode Remote Containers.

>  Do **not** use these commands within the Skills Network Cloud IDE. They are strictly for **local development**.

---

##  Prerequisites

Ensure the following tools are installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com)
  - with the extension [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [K3D (Kubernetes in Docker)](https://k3d.io/)
- Optionally: [Homebrew](https://brew.sh/) or [Chocolatey](https://chocolatey.org/) for installation automation

---

##  Local Setup Commands

### 1. Start a local K3D Kubernetes cluster

```bash
make cluster
```

### 2. Install Tekton Pipelines

```bash
make tekton
```

### 3. Install IBM Cloud IDE ClusterTasks

```bash
make clustertasks
```

You’re now ready to use Tekton pipelines on your local Kubernetes cluster just like in the IBM lab environment.

---

##  Why K3D?

K3D provides a lightweight Kubernetes cluster that runs inside Docker. It's ideal for local DevOps testing, CI/CD pipeline simulation, and learning Kubernetes without needing a cloud provider.

---

##  Related Skills Demonstrated

- Infrastructure as Code via Makefile
- Kubernetes simulation using K3D
- CI/CD pipelines with Tekton
- Tekton Task and ClusterTask configuration
- Developer productivity via VSCode Remote Containers

---

##  Author

Crafted with ❤️ by [Guy Landry Djolaud](https://github.com/guylandrydjolaud)  
 Contact: guylandry.djolaud@gmail.com  
 Portfolio: [devoptimize.tech](https://devoptimize.tech)

---

##  License

Apache License 2.0 – see [LICENSE](LICENSE)

---

## <h3 align="center">© IBM Corporation 2022 | Customized for educational and portfolio purposes.</h3>
