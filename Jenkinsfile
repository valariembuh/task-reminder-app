pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/valariembuh/task-reminder-app.git'
            }
        }

        stage('Check Environment') {
            steps {
                sh 'python --version || true'
                sh 'pip --version || true'
                sh 'docker --version || true'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test App') {
            steps {
                sh 'python -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-reminder-app .'
            }
        }
    }
}
