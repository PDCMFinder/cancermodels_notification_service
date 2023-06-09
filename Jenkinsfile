pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'Building'
                echo 'python version is .. '
                sh 'python --version'
                sh 'ls -ls /usr/bin/python*'
            }
        }
    }
}
