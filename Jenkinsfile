pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t flask-mysql-appss .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop flask-container || true'
                sh 'docker rm flask-container || true'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker run -d \
                  --name flask-container \
                  -p 5000:5000 \
                  flask-mysql-appss
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }

        failure {
            echo '❌ Deployment Failed!'
        }

        always {
            sh 'docker ps -a'
        }
    }
}
