
pipeline {
    agent any

    envirement {
        PYTHON_HOME = 'C:/Program Files/Python310'
        PATH = "${env.PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Run Api') {
            steps {
                sh 'python Api.py'
            }
        }
        stage('Api Test') {
            steps {
                echo 'Testing..'
                sh 'python ApiTest.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying..'
            }
        }
    }
}