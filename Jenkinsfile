pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                script {
                    git url: 'https://github.com/nackc8/cicd-grp--apple.git', branch: 'oskar', credentialsId: 'github-access-token-id'
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

        stage('Building docker image') {
            steps {
                script {
                    echo "Building image..."
                    sh 'docker build -t py-flask-server -f backend/Dockerfile backend'
                }
            }
        }

        stage('Start container') {
            steps {
                script {
                    echo "Starting container..."
                    sh 'docker run -d -p 5000:5000 --name pingurl-server py-flask-server'
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    echo "Pytesting watched-url..."
                    sh '''
                    pytest backend/test_api_req.py
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