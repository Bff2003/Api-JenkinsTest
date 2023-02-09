
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('api') {
                    sh 'npm install'
                }
            }
        }
        
        stage('Test') {
            steps {
                dir('api') {
                    sh 'npm start test'
                }
            }
        }

        stage('Deploy') {
            steps {
                dir('api') {
                    sh 'npm start &'
                }
            }
        }
    }
}