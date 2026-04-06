pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "dhivyalakshmir"
        IMAGE_NAME = "expense"
    }

    stages {
        stage('Clone') {
            steps {
                git branch: "${BRANCH_NAME}", url: 'https://github.com/dhivyathirisha138-sudo/expense-tracker.git'
            }
        }

        stage('Set Tag') {
            steps {
                script {
                    if (env.BRANCH_NAME == "v1") {
                        env.TAG = "v1"
                    } else if (env.BRANCH_NAME == "v2") {
                        env.TAG = "v2"
                    } else if (env.BRANCH_NAME == "v3") {
                        env.TAG = "v3"
                    }
                }
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
                    bat "echo %PASS% | docker login -u %USER% --password-stdin"
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