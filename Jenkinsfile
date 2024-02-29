pipeline {
    agent any
    
    triggers {
        githubPush()
        // scm 'refs/heads/main'
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
                sh 'pip install pytest'
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
                branch 'master'
            }
            steps {
                echo 'Deploying to staging environment...'
                script {
                    currentBuild.result = "SUCCESS" // Set the result to SUCCESS initially
                    try {
                        // Your deployment logic goes here
                        echo 'Deploying to staging environment...'
                        // Example: deploy command
                        // sh 'fab deploy'
                    } catch (Exception e) {
                        // If deployment fails, mark the build as FAILURE
                        currentBuild.result = "FAILURE"
                        throw e
                    }
                }
            }
        }
    }

    post {
        success {
            emailext (
                subject: "Build Success",
                body: "Jenkins CI CD pipeline for flask application build was successful.",
                to: "gupta.surender.1990@gmail.com"
            )
        }
        failure {
            emailext (
                subject: "Build Failure",
                body: "The build failed of Jenkins CI CD pipeline for flask application.",
                to: "gupta.surender.1990@gmail.com"
            )
        }
    }
}
