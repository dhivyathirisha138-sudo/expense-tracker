pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "dhivyathirisha138-sudo"
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
                sh "docker build -t $DOCKERHUB_USER/$IMAGE_NAME:$TAG ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DHIVYALAKSHMIR',
                    passwordVariable: 'Lakshmi#123'
                )]) {
                    sh 'echo $Lakshmi#123 | docker login -u $DHIVYALAKSHMIR --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push $DOCKERHUB_USER/$IMAGE_NAME:$TAG"
            }
        }
    }
}