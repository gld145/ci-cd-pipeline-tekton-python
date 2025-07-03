# Cloud-Native CI/CD System with Tekton for Python Microservice

[![CI Build](https://img.shields.io/badge/CI-Build%20Passing-brightgreen)]()
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)]()
[![Python](https://img.shields.io/badge/Python-3.9-blueviolet)]()
[![Testing](https://img.shields.io/badge/Testing-TDD%20%26%20BDD-orange)]()
[![Author](https://img.shields.io/badge/Made%20by-Guy%20Landry%20Djolaud-darkgreen)]()

This repository contains a final project that demonstrates a complete **Cloud-Native CI/CD** pipeline  
with a strong emphasis on software quality through **Test-Driven Development (TDD)** and  
**Behavior-Driven Development (BDD)** practices.

> Built using **Python**, deployed using modern DevOps practices  
> in a microservice architecture inspired by production-level workflows.
>
> **Created by Guy Landry Djolaud** — DevOps Architect focused on Cloud, Automation, and Containerization.

---

## Key Features

- Python microservice using Flask & PostgreSQL
- RESTful API built with MVC design pattern
- Unit tests with `pytest` ensuring >95% code coverage
- Tekton pipelines for CI/CD orchestration
- Docker containerization & Kubernetes manifests
- YAML-based IaC with reusable templates

---

## Dev Environment Setup

This was developed in the IBM Skills Network Cloud IDE with OpenShift. To recreate the environment locally:

```bash
source bin/setup.sh
```

This initializes:
- Python 3.9 with `venv`
- Virtual environment activation
- CLI prompts for DevOps workflow

Activate environment:

```bash
source ~/venv/bin/activate
```

Install dependencies:

```bash
make install
```

Run PostgreSQL container:

```bash
make db
```

---

## Project Structure

```text
├── service/             # Flask microservice
│   ├── models.py        # Business logic
│   └── routes.py        # REST API endpoints
├── tests/               # Unit tests
├── tekton/              # Tekton pipeline definitions
├── deploy/              # Kubernetes YAML manifests
├── Dockerfile           # Container image spec
├── Makefile             # Build/test/run automation
└── bin/setup.sh         # Dev environment bootstrapper
```

---

## Local Kubernetes Simulation

To replicate the IBM Cloud IDE locally:

```bash
make cluster      # Start K3D cluster
make tekton       # Install Tekton
make clustertasks # Add IBM’s ClusterTasks
```

Use Docker Desktop + VS Code + Remote Containers for full local experience.

---

## Data Model (Account)

| Field         | Type         | Required |
|---------------|--------------|----------|
| id            | Integer      | Yes      |
| name          | String(64)   | Yes      |
| email         | String(64)   | Yes      |
| address       | String(256)  | Yes      |
| phone_number  | String(32)   | Optional |
| date_joined   | Date         | Yes      |

---

## About This Project

This project was built using Test Driven Development (TDD). Features were added by first writing the test, then developing the code to satisfy test cases. Tools used include:

- GitHub Actions
- Tekton CI/CD Pipelines
- OpenShift Deployment
- Docker Containers
- Postgres for persistent storage

---

## Author

**Guy Landry Djolaud**  
DevOps | Platform Engineering | AWS | Kubernetes  
🔗 [LinkedIn](https://www.linkedin.com/in/guy-landry-djolaud-1037a8311) • [GitHub](https://github.com/gld145)

---

## 📄 License

Licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.

---

 Last Updated: July 03, 2025
