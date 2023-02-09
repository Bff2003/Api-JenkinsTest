
pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:/"Program Files"/Python310'
        PATH = "${env.PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Run Api') {
            steps {
                echo "${PYTHON_HOME}/python.exe Api.py"
                sh "${PYTHON_HOME}/python.exe Api.py"
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