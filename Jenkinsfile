def flag = false;

pipeline {
    agent any
    
    environment {
        GITHUB_URL = 'https://github.com/surendergupta/jenkins_CI_CD_pipeline_for_flask_application.git'
        GITHUB_BRANCH = 'master'
        SSH_USER = 'ubuntu'
        SERVER_IP = '3.91.38.111'
    }

    triggers {
       githubPush()
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh '/usr/bin/python3 -m pytest test.py'
                script { flag = true }
            }
        }
        stage('Deploy to Staging') {
            when { expression { flag == true } }
            steps {
                script {                                    
                    sshagent(credentials: ['i-0ae1203560d674bb6']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} '
                            sudo apt-get update -y &&
                            sudo apt install python3-pip -y &&
                            python3 -m pip install --upgrade pip &&
                            sudo mkdir -p /home/ubuntu/FlaskApp/ &&
                            sudo chmod 777 /home/ubuntu/FlaskApp/ &&
                            cd /home/ubuntu/FlaskApp/ &&
                            scp -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/jenkins_pipeline/* . &&                            
                            pip install -r requirements.txt && 
                            sudo kill -9 $(sudo lsof -t -i:5000) || true &&
                            nohup python3 app.py > output.log 2>&1 & '
                        '''
                        echo "Flask App deployed to AWS Server"
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
