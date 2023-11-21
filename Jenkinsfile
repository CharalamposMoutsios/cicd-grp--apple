pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = credentials('dbb73c93-9344-42a4-b151-72bc8e517dea')
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
                    git credentialsId: GITHUB_CREDENTIALS, url: 'https://github.com/nackc8/cicd-grp--apple.git'
                }
            }
        }

        stage('Install pylint') {
            steps {
                script {
                    sh 'pip install pylint'
                }
            }
        }

        stage('Build image') {
            steps {
                script {
                    sh 'docker pull py_flask_server'
                }
            }
        }

        stage('Run pylint') {
            steps {
                script {
                    sh 'pylint --rcfile=backend/.pylintrc backend/pingurl/*.py backend/app.py'
                }
            }
        }

        stage('Start container') {
            steps {
                script {
                    sh 'docker run -d --name jenkins_pingurl -p 5000:5000 py_flask_server'
                }
            }
        }
    }

    post {
        failure {
            echo 'Build failed. Try to fix it?'
        }
    }
}