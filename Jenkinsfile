pipeline {
    agent any
    environment {
        db_creds = credentials('4cf4078c-4a59-4919-808e-863c9c9eee85')
    }
    stages {
        stage('run backend server') {
            steps {
                bat("start /min python rest_app.py " + $db_creds + " " + $db_creds_PSW)
            }
        }
        stage('run frontend server') {
            steps {
                bat("start /min python web_app.py " + $db_creds + " " + $db_creds_PSW)
            }
        }
        stage('Backend testing') {
            steps {
                bat 'python backend_testing.py'
            }
        }
        stage('Frontend testing') {
            steps {
                bat 'python frontend_testing.py'
            }
        }
        stage('Combined testing') {
            steps {
                bat 'python combined_testing.py'
            }
        }
        stage('Clean environment') {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }
        post{
         failure{
         mail to: "broder.guy@gmail.com",
         subject: "Jenkins failed pipeline test",
         body: "Jenkins failed pipeline test"
         }
     }
}
