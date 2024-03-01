pipeline {
    agent any
    
    environment {
        GITHUB_URL='https://github.com/surendergupta/jenkins_CI_CD_pipeline_for_flask_application.git'
        GITHUB_BRANCH = 'master'
        SSH_USER = 'ubuntu'
        SERVER_IP = '44.223.28.116'
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Repo Clone') {
            steps {
                git branch: env.GITHUB_BRANCH, url: env.GITHUB_URL
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test.py'
            }
        }
        stage('Deploy to EC2') {
            steps {
                script {
                    sshagent(credentials: ['44.223.28.116']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} '
                            sudo apt-get update -y &&
                            sudo mkdir -p /home/ubuntu/FlaskApp/ &&
                            cd /home/ubuntu/FlaskApp/ &&                            
                            ls'
                        '''
                        echo "Flask App deployed to AWS Server"
                    }
                }                
            }
        }        
    }
}
