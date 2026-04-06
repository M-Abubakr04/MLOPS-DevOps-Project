# 🚀 ML DevOps Pipeline with GitHub Actions, Docker & Kubernetes

## 📌 Overview

This project demonstrates a complete **MLOps (Machine Learning Operations) pipeline** using:

* GitHub Actions (CI/CD)
* Docker (Containerization)
* Kubernetes (Deployment)
* Flask API (Model Serving)

The pipeline automates:

* Model training
* Model testing
* Docker image building
* Image push to DockerHub
* Deployment on Kubernetes (Minikube)

---

## 🧠 Architecture

```
Code Push → GitHub Actions →
Train Model → Test Model →
Build Docker Image → Push to DockerHub →
Deploy on Kubernetes → Serve via API
```

---

## 📂 Project Structure

```
ml-devops-project/
│
├── model.py              # Train ML model
├── test_model.py         # Test model accuracy
├── app.py                # Flask API for predictions
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container configuration
├── deployment.yaml       # Kubernetes Deployment
├── service.yaml          # Kubernetes Service
│
└── .github/
    └── workflows/
        └── main.yml      # GitHub Actions CI/CD pipeline
```

---

## ⚙️ Technologies Used

* Python
* Scikit-learn
* Flask
* Docker
* Kubernetes (Minikube)
* GitHub Actions

---

## 🧪 Machine Learning Model

* Dataset: Iris Dataset
* Model: Logistic Regression
* Output: Saved as `iris_model.pkl`

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/ml-devops-project.git
cd ml-devops-project
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Locally

Train model:

```
python model.py
```

Test model:

```
python test_model.py
```

Run API:

```
python app.py
```

---

## 🐳 Docker Setup

### Build Image

```
docker build -t YOUR_DOCKERHUB_USERNAME/ml-app .
```

### Run Container

```
docker run -p 5000:5000 YOUR_DOCKERHUB_USERNAME/ml-app
```

---

## ☸️ Kubernetes Deployment

### Start Minikube

```
minikube start --driver=docker
```

### Deploy App

```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Check Status

```
kubectl get pods
kubectl get services
```

### Access App

```
minikube service ml-service
```

---

## 🔄 GitHub Actions CI/CD Pipeline

The pipeline runs automatically on every push to `main` branch:

### ✔ Steps:

* Install dependencies
* Train model
* Test model
* Build Docker image
* Push to DockerHub

---

## 🔐 GitHub Secrets Required

Add in **GitHub → Settings → Secrets → Actions**

* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`

---

## 🧪 API Testing

Example request:

```
curl -X POST http://<URL>/predict \
-H "Content-Type: application/json" \
-d '{"features":[5.1,3.5,1.4,0.2]}'
```

Response:

```
{"prediction": 0}
```

---

## ⚠️ Common Issues

* Docker permission error → `newgrp docker`
* Pod not running → `kubectl logs <pod-name>`
* Image not pulling → check DockerHub credentials
* Minikube slow → normal on low RAM systems

---

## 📈 Future Improvements

* Add automatic Kubernetes deployment via GitHub Actions
* Integrate MLflow for experiment tracking
* Use Helm charts
* Deploy on AWS / GCP

---

## 🎯 Learning Outcomes

By completing this project, you understand:

* CI/CD for ML workflows
* Containerization using Docker
* Kubernetes deployment
* Building production-ready ML APIs

---

## 👨‍💻 Author

**M. Abubakr**
Aspiring Penetration Tester & DevOps Learner

---

## ⭐ Support

If you found this helpful, give this repo a ⭐ on GitHub!

---
