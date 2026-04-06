pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "DHIVYALAKSHMIR"
        IMAGE_NAME = "expense"
        TAG = "v1"
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'v1', url: 'https://github.com/dhivyathirisha138-sudo/expense-tracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKERHUB_USER%/%IMAGE_NAME%:%TAG% ."
            }
        }
        stage('Login to DockerHub') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'USER',
            passwordVariable: 'PASS'
        )]) {
            bat '''
            docker login -u %USER% -p %PASS%
            '''
        }
    }
}

       

        stage('Push Docker Image') {
            steps {
                bat "docker push %DOCKERHUB_USER%/%IMAGE_NAME%:%TAG%"
            }
        }
    }
}