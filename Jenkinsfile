pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/valariembuh/task-reminder-app.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test Application') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-reminder-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker stop task-reminder-app || true
                    docker rm task-reminder-app || true
                    docker run -d -p 8080:8080 --name task-reminder-app task-reminder-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
