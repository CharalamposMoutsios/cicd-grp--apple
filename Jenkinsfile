pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                script {
                    git url: 'https://github.com/nackc8/cicd-grp--apple.git', branch: 'main'
                }
            }
        }

        stage('Building docker image') {
            steps {
                script {
                    echo "Building image..."
                    sh 'docker build -t py-flask-server -f backend/Dockerfile backend'
                }
            }
        }

        stage('Removing previous container') {
            steps {
                script {
                    echo "Stopping & removing old pingurl-server"
                    sh '''
                    pwd &&
                    ls &&
                    ./docker_step.sh
                    '''
                }
            }
        }

        stage('Start container') {
            steps {
                script {
                    echo "Starting container..."
                    sh 'docker run -d -p 5000:5000 --network=jenkins_jenkins_default --name pingurl-server py-flask-server'
                }
            }
        }

        stage('Contacting pingurl server') {
            steps {
                script {
                    // Debug step to check if connection is established to pingurl-server
                    echo "Contacting pingurl..."
                    sh 'hostname'
                    sh 'curl pingurl-server.jenkins_jenkins_default:5000'
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    echo "Getting container ip & pytesting..."
                    sh '''
                    . ./get_container_ip.sh &&
                    ./pytest_step.sh
                    '''
                }
            }
        }

        stage('Run Pylint') {
            steps {
                echo "Pylinting the code..."
                sh '''
                cd backend && pylint --fail-under 6 pingurl/ --rcfile=./.pylintrc
                '''
            }
        }

        stage('Stop container') {
            steps {
                script {
                    sh '''
                    docker stop pingurl-server
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Build succeeded, woop woop!"
        }
        failure {
            echo 'Build failed. Try to fix it?'
        }
    }
}