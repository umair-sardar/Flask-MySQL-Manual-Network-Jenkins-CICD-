# 🚀 Flask + MySQL with Jenkins CI/CD

A simple DevOps project demonstrating a **Flask web application** connected to a **MySQL database**, with automated **build and deployment** using **Jenkins CI/CD**.

## 🛠️ Tech Stack

- Python Flask
- MySQL
- Docker
- Jenkins
- Git & GitHub
- Linux (Ubuntu)

## 📂 Project Structure

```
flask-mysql/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── template/
│       └── index.html
├── db/
│   └── init.sql
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## 🚀 Workflow

1. Push code to GitHub
2. Jenkins automatically pulls the latest code
3. Docker builds the Flask image
4. Existing container is removed
5. New container is deployed automatically

## ✨ Features

- Flask Web Application
- MySQL Database Integration
- Dockerized Deployment
- Jenkins CI/CD Automation
- Automatic Container Deployment

## 📸 Project Screenshot

Store your project screenshots inside the **Screenshot/** folder.

## 👨‍💻 Author

**Umair Sardar**

⭐ If you found this project useful, don't forget to star the repository.
