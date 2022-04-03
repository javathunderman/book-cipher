pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            steps {
                withEnv(['PATH+EXTRA=/home/arjun/.local/bin']) {
                    sh '''
                        pip3 install pyinstaller PySimpleGUI pdftotext && cd src && pyinstaller main.py
                    '''
                }
            }
        }
    }
}
