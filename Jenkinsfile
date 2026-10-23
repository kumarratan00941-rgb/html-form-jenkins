
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh 'python3 -m unittest -v test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed.'
        }
        failure {
            echo 'FAILURE: Check the console output for errors.'
        }
        always {
            echo 'Jenkins pipeline execution completed.'
        }
    }
}
