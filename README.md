# Python Flask API Server Project

## Overview

This project is a Python Flask-based API server designed for managing user data. It includes a Dockerized setup for consistent deployment and is configured to run on a Minikube Kubernetes cluster. Additionally, a CI/CD pipeline using GitHub Actions is implemented for automated testing and deployment.

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Minikube
- kubectl
- A GitHub account

### Local Setup and Run

1. **Clone the Repository**:
2. **Navigate to the Project Directory**:
3. **Create and Activate a Virtual Environment**:
- Windows: `python -m venv venv` then `venv\Scripts\activate`
- Unix/MacOS: `python3 -m venv venv` then `source venv/bin/activate`
4. **Install Dependencies**:
  pip install -r requirements.txt
5. **Initialize the Database**:
```python
from app import db
db.create_all()
```
or use the init_db.py
6. **Run the application**
```python
python run.py
```

The server will start running on http://localhost:5000

**API Endpoints**

***Create User***

- URL: /api/users
- Method: POST
- Data Params:
```
{
    "username": "string",
    "email": "string",
    "password": "string"
}
```
- Success Response:
- Code: 201 CREATED
- Content:
```
{
    "id": "integer",
    "username": "string",
    "email": "string"
}
```
- Error Response:
- Code: 400 BAD REQUEST
- Content: {"error": "Missing data"}

*** Get User by ID***

- URL: /api/users/<user_id>
- Method: GET
- URL Params: user_id = integer
- Success Response:
- Code: 200 OK
- Content:
```
{
    "id": "integer",
    "username": "string",
    "email": "string"
}
```
- Error Response:
- Code: 404 NOT FOUND
- Content: {"error": "User not found"}

***Get All Users***

- URL: /api/users
- Method: GET
- Success Response:
- Code: 200 OK
- Content:
```
[    {        "id": "integer",        "username": "string",        "email": "string"    },    ...]
```
- This API server is intended for demonstration purposes and is not configured for production use.



### Dockerisation
1. **Build the docker image**:
```
docker build -t python-flask-api .
```
2. **Run the Docker Container**:
```
docker run -p 8080:80 python-flask-api
```

### Deploying to Minikube
1. **Start Minikube**:
```
minikube start
```
2. **Set Docker Environment**:
```
eval $(minikube docker-env)
```
3. **Build the Docker Image in Minikube**:
```
docker build -t python-flask-api:latest .
```
4. **Apply Kubernetes Manifests**:
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
5. **Access the Service**:
- Get the Minikube IP: minikube ip
- Access the service at http://<minikube-ip>:<node-port>

### CI/CD Pipeline with GitHub Actions
This project uses GitHub Actions for Continuous Integration and Continuous Deployment. The workflow is defined in .github/workflows/ci-cd.yml and includes the following stages:

**Build***: Installs dependencies and prepares the build.
**Dockerize**: Builds a Docker image of the API server.
**Deployment**: Simulates deployment to a Minikube cluster.
**Pipeline Execution**: Triggered on every push to the repository, executing the defined pipeline.
**Simulation**: Minikube commands in the pipeline wont actually run. Either should we deployed to a kubernetes cluster on cloud or even ECS or a VM
