ipipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/valariembuh/task-reminder-app.git'
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
                sh 'docker build -t task-reminder-app:latest .'
            }
        }

    }
}
