pipeline {
    agent { docker { image 'python:3.10.7-alpine' } }
    stages {
        stage('build') {
            steps {
                echo 'Building'
                echo 'python version is .. '
                sh 'python --version'
            }
        }
    }
}
