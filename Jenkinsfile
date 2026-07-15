pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
               git 'https://github.com/umair-sardar/Flask-MySQL-Manual-Network-Jenkins-CICD-.git'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t flask-mysql-appss .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
                sh '''
                docker run -d \
                  --name flask-container \
                  --network my-custom-network \
                  -p 5000:5000 \
                  -e DB_HOST=mysql-container \
                  -e DB_USER=root \
                  -e DB_PASSWORD=rootpassword \
                  -e DB_NAME=mydb \
                  flask-mysql-app
                '''
            }
        }
    }
}
