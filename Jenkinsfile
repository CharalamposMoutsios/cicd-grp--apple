pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                script {
                    git url: 'https://github.com/nackc8/cicd-grp--apple.git', branch: 'oskar' //, credentialsId: 'github-access-token-id'
                }
            }
        }

        // I have sh 'hostname' in each step for debugging connection issues between Jenkins & Flask

        stage('Building docker image') {
            steps {
                script {
                    echo "Building image..."
                    sh 'hostname'
                    sh 'docker build -t py-flask-server -f backend/Dockerfile backend'
                }
            }
        }

        stage('Start container') {
            steps {
                script {
                    echo "Starting container..."
                    sh 'hostname'
                    sh 'docker run -d -p 5000:5000 --network=jenkins_jenkins_default --name pingurl-server py-flask-server'
                }
            }
        }

        stage('Contacting pingurl server') {
            steps {
                script {
                    // Added this step in attempts to establish connection between Jenkins and Flask
                    // There have been connection issues between the two when attempting to run
                    // the 'Run Pytest' step, hoping this could maybe give some insight into IP, etc.
                    echo "Contacting pingurl..."
                    sh 'hostname'
                    sh 'curl pingurl-server.jenkins_jenkins_default:5000'
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    echo "Pytesting watched-url..."
                    sh 'hostname'
                    sh 'echo "Shell: $SHELL"'
                    sh 'source venv/bin/activate'
                    sh '''
                    pytest ./backend/tests/test_api_req.py
                    '''
                }
            }
        }

        stage('Run Pylint') {
            steps {
                echo "Pylinting the code..."
                sh 'hostname'
                sh '''
                cd backend && pylint --fail-under 6 pingurl/ --rcfile=./.pylintrc
                '''
            }
        }

        stage('Stop container') {
            steps {
                script {
                    sh 'hostname'
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

        // Don't know if I should keep this or scrap it.
        // stage('Installing requirements.txt') {
        //     steps {
        //         echo "Installing requirements"
        //         // Create a virtual environment
        //         sh 'python3 -m venv venv'

        //         // Activate the virtual environment
        //         sh 'source venv/bin/activate'

        //         // Install requirements inside the virtual environment
        //         sh 'pip install -r backend/requirements.txt'

        //         // Deactivate the virtual environment
        //         sh 'deactivate'
        //     }
        // }


        // stage('Creating virtual environment') {
        //     steps {
        //         echo "Creating venv..."
        //         sh '''
        //         cd backend && rm -rf venv && python3 -m venv venv
        //         chmod +x venv/bin/activate
        //         venv/bin/activate && pip install -r requirements.txt
        //         '''
        //     }
        // }