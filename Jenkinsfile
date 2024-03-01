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
                            sudo apt install python3-pip -y &&
                            python3 -m pip install --upgrade pip &&
                            sudo mkdir -p /home/ubuntu/FlaskApp/ &&
                            sudo chmod 777 /home/ubuntu/FlaskApp/ &&
                            cd /home/ubuntu/FlaskApp/ &&
                            scp -o StrictHostKeyChecking=no -r /var/lib/jenkins/workspace/jenkins_pipeline/* . &&                            
                            pip install -r requirements.txt && 
                            sudo kill -9 $(sudo lsof -t -i:5000) || true &&
                            nohup python3 app.py > output.log 2>&1 & &&
                            ls'
                        '''
                        echo "Flask App deployed to AWS Server"
                    }
                }                
            }
        }        
    }
}
