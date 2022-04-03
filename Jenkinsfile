pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Build') {
            withEnv(['PATH+EXTRA=/home/arjun/.local/bin']) {
                steps {
                    sh '''
                        pip3 install pyinstaller PySimpleGUI pdftotext && cd src && pyinstaller main.py
                    '''
                }
            }
        }
    }
}
