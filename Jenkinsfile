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

        stage('Creating virtual environment') {
            steps {
                echo "Creating venv..."
                sh '''
                cd backend && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
                '''
            }
        }


        stage('Building docker image') {
            steps {
                script {
                    echo "Building image..."
                    sh 'docker build -t py-flask-server -f backend/Dockerfile .'
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
                    echo "Pytesting backend..."
                    sh '''
                    source ./backend/venv/bin/activate && pytest backend/
                    '''
                }
            }
        }

        stage('Run Pylint') {
            steps {
                echo "Pylinting the code..."
                sh '''
                source ./backend/venv/bin/activate && pylint --fail-under 10 backend/pingurl/ --rcfile=backend/.pylintrc
                '''
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