pipeline {
    agent any
    
    triggers {
        scm 'refs/heads/main'
        // Polls the SCM every minute for changes
        // pollSCM('* * * * *') 
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest test.py'
            }
            post {
                always {
                    junit '**/test-results/*.xml'
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to staging environment...'
                // Add deployment commands here
            }
        }
    }

    post {
        success {
            emailext (
                subject: "Build Success",
                body: "Jenkins CI CD pipeline for flask application build was successful.",
                to: "$DEFAULT_RECIPIENTS"
            )
        }
        failure {
            emailext (
                subject: "Build Failure",
                body: "The build failed of Jenkins CI CD pipeline for flask application.",
                to: "$DEFAULT_RECIPIENTS"
            )
        }
    }
}
