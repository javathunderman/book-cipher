pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            steps {
                sh '''
                	pip3 install pyinstaller PySimpleGUI pdftotext && cd src && pyinstaller main.py
                '''
            }
        }
    }
}
