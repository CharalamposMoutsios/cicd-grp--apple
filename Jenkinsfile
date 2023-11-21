pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = credentials('github-access-token-id')
        GIT_EXECUTABLE = "${tool 'Default'}"
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
                    withEnv(["GIT_ASKPASS=echo", "GIT_EXECUTABLE=${GIT_EXECUTABLE}"]) {
                        git credentialsId: 'github-access-token-id', url: 'https://github.com/nackc8/cicd-grp--apple.git'
                    }
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

        stage('Run pylint') {
            steps {
                script {
                    sh 'pylint --rcfile=backend/.pylintrc backend/pingurl/*.py backend/app.py'
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