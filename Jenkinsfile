
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
        
        stage('Turn on') {
            steps {
                dir('api') {
                    sh 'npm start'
                }
            }
        }
    }
}