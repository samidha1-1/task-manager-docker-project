#  Task Manager - Docker & Kubernetes Project

A containerized Task Manager web application built with **Flask** and **MySQL**. The project demonstrates how to package an application using Docker, orchestrate multiple containers with Docker Compose, and deploy the application on Kubernetes.

---

##  Tech Stack

- Python (Flask)
- MySQL
- Docker
- Docker Compose
- Kubernetes
- Minikube
- kubectl

---

##  Project Structure

```
task-manager-docker-project/
│
├── app/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── k8s/
    ├── app-deployment.yml
    ├── app-service.yml
    ├── mysql-deployment.yml
    ├── mysql-service.yml
    ├── ingress.yml
    ├── config.yml
    └── secrets.yml
```

---

## Features

- Create and manage tasks
- Flask backend with MySQL database
- Containerized using Docker
- Multi-container deployment using Docker Compose
- Kubernetes Deployment and Service manifests
- Scalable application architecture

---

## Docker Deployment

### Build the Docker image

```bash
docker build -t task-manager .
```

### Run using Docker Compose

```bash
docker compose up -d
```

Verify running containers:

```bash
docker ps
```

---

## Kubernetes Deployment

Apply all Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Verify resources:

```bash
kubectl get pods
kubectl get deployments
kubectl get services
```


## Learning Outcomes

- Wrote a production-ready Dockerfile
- Built and managed Docker images
- Used Docker Compose for multi-container applications
- Created Kubernetes Deployments
- Exposed applications using Kubernetes Services
- Verified application deployment using kubectl

---

## Author

**Samidha Wani**

GitHub: https://github.com/samidha1-1
