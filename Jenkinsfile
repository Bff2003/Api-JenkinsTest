
pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:/Program Files/Python310/python.exe'
        PATH = "${env.PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Run Api') {
            steps {
                sh '${PYTHON_HOME} Api.py'
                echo "${env.PYTHON_HOME};${env.PATH}"
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