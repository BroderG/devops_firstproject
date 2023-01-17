pipeline {
    agent any
    stages {
        stage('run backend server') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage('run frontend server') {
            steps {
                bat 'start /min python web_app.py'
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
         always{
         mail to: "broder.guy@gmail.com",
         subject: "Test Jenkins Email",
         body: "Test"
         }
     }
}
