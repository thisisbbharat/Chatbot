pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t chatbot .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run chatbot python -m unittest test_chatbot.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
