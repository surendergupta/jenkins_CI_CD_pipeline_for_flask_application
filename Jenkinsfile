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
        stage('Deploy to EC2') {
            steps {
                script {
                    sshagent(credentials: [SERVER_IP]) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} '
                            sudo apt-get update -y &&
                            sudo mkdir -p /home/ubuntu/FlaskApp/ &&
                            cd /home/ubuntu/FlaskApp/ &&
                            scp -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/jenkins_pipeline ${SSH_USER}@${SERVER_IP}:/home/ubuntu/FlaskApp/
                            ls'
                        '''
                        echo "Flask App deployed to AWS Server"
                    }
                }                
            }
        }        
    }
}
