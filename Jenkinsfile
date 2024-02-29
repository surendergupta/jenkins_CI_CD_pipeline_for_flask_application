pipeline {
    agent any
    
    environment {
        SSH_USER = 'ubuntu'
        SERVER_IP = '35.175.149.165'
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Build') {
            steps {
                sshagent(credentials: ['i-0a28f03c1430551f3']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} '
                        sudo apt-get update -y &&
                        sudo apt-get install python3-pip &&
                        sudo pip3 install virtualenv && 
                        virtualenv venv &&
                        source venv/bin/activate &&
                        cd /home/ubuntu/ &&
                        git clone https://github.com/surendergupta/jenkins_CI_CD_pipeline_for_flask_application.git &&
                        cd jenkins_CI_CD_pipeline_for_flask_application &&
                        pip3 install -r requirements.txt'
                    echo "Flask App to AWS Server"
                    '''
                }                
            }
        }
        
        stage('Test') {
            steps {
                sshagent(credentials: ['i-0a28f03c1430551f3']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} '
                        source myenv/Scripts/activate &&
                        cd jenkins_CI_CD_pipeline_for_flask_application &&
                        pip3 install -r requirements.txt &&
                        pytest test.py'
                    echo "Flask App Testing using Pytest"
                    '''
                }
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
                sshagent(credentials: ['i-0a28f03c1430551f3']) {
                    script {
                        currentBuild.result = 'SUCCESS'
                        try {
                            sh '''
                            ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} '
                                cd jenkins_CI_CD_pipeline_for_flask_application &&
                                nohup python3 app.py &'                            
                            echo "Flask App Running"'
                            '''
                        } catch (Exception e) {
                            // If deployment fails, mark the build as FAILURE
                            currentBuild.result = 'FAILURE'
                            throw e
                        }
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
