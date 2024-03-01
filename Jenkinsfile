pipeline {
    agent any
    
    environment {
        GITHUB_URL='https://github.com/surendergupta/jenkins_CI_CD_pipeline_for_flask_application.git'
        GITHUB_BRANCH = 'master'
        SSH_USER = 'ubuntu'
        SERVER_IP = '3.91.38.111'
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Deploy to EC2') {
            steps {
                script {
                    sshagent(credentials: ['i-0ae1203560d674bb6']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} '
                            sudo apt-get update -y &&
                            sudo mkdir -p /home/ubuntu/FlaskApp/ &&
                            cd /home/ubuntu/FlaskApp/ &&
                            scp -o StrictHostKeyChecking=no -r ${SSH_USER}@${SERVER_IP}:/var/lib/jenkins/workspace/jenkins_pipeline/* . &&
                            ls'
                        '''
                        echo "Flask App deployed to AWS Server"
                    }
                }                
            }
        }        
    }
}
