pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/valariembuh/task-reminder-app.git'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Test App') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t task-reminder-app:latest .'
            }
        }
    }
}
