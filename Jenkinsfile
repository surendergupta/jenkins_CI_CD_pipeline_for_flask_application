pipeline {
    agent any
    
    environment {
        SSH_USER = 'ubuntu'
        SERVER_IP = '44.223.28.116'
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Build') {
            steps {
                script {
                    sshagent(credentials: ['your-ssh-credentials-id']) {
                        sh '''
                        ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SERVER_IP} << 'ENDSSH'
                            sudo apt-get update -y &&
                            cd /home/ubuntu/ &&
                            # Additional commands here
                        ENDSSH
                        '''
                        echo "Flask App deployed to AWS Server"                    
                    }
                }                
            }
        }
        
    }
}
