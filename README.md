# Flask Application CI/CD Pipeline with Jenkins

This repository contains a sample Flask application along with a Jenkins CI/CD pipeline setup to automate the testing and deployment process.

## Prerequisites

Before setting up the Jenkins pipeline, ensure you have the following prerequisites installed:

- Jenkins: Install Jenkins on a virtual machine or use a cloud-based Jenkins service.
- Python: Ensure Python is installed on the machine where Jenkins is running.
- Pip: Python package manager.
- Git: Version control system for cloning the repository.

## Setup:
- Install Jenkins on a virtual machine or use a cloud-based Jenkins service.	
- Launch EC2 Instance and Open 8080 Port on it.	
- First Install Java
	```	sudo apt update
		sudo apt install fontconfig openjdk-17-jre
		java -version
	```
		
- After Install Java Install Jenkin to EC2 Instance or virtual machine
	```
		sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
			https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
		echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
			https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
			/etc/apt/sources.list.d/jenkins.list > /dev/null
		sudo apt-get update
		sudo apt-get install jenkins
	```

## Start Jenkins

- You can enable the Jenkins service to start at boot with the command:
```
  sudo systemctl enable jenkins
```
- You can start the Jenkins service with the command:
```
  sudo systemctl start jenkins
```
- You can check the status of the Jenkins service using the command:
```
  sudo systemctl status jenkins
```
- You can see Jenkins 
```
  http:<Instance_public_ip_address>:8080
```
- You can see and enter jenkin usng this command in terminal:
```
  sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
- Output like this you can copy and Enter and click continue:
```
  e2c729ac93f74666976b875ffb18cb86
```
- You can choose install plugin recommended Steps and Create User and remember Password;
- Now make sure Jenkins is up and running.

## Install Python Plugins in Jenkins Server
# Configure Jenkins with Python and any necessary libraries.
- IF python not install please install then pip
- Command to install necessary libraries:
```
		sudo apt install python3-pip -y
		pip3 install Flask
		pip3 install pytest
```

## Create Jenkins Pipeline:
- Create a Jenkinsfile in the root of your Python application repository.
- Define the pipeline stages: Build, Test, and Deploy.
- Configure triggers to trigger a build on changes to the main branch.
