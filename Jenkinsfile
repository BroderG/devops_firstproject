pipeline {
    agent any
    stages {
        stage('install packages') {
            steps {
                bat 'pip install requests'
                bat 'pip install pymysql'
                bat 'pip install json'
                bat 'pip install time'
            }
        }
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
}
