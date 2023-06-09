pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Building'
                sh 'docker --version'
                echo 'python version is .. '
                sh 'python --version'
            }
        }
    }
}
