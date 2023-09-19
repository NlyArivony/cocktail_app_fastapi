#!/bin/bash

# Update the package lists once at the beginning
sudo apt update

# Install OpenJDK 17
sudo apt install openjdk-17-jre -y

# Install Jenkins
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo gpg --dearmor -o /usr/share/keyrings/jenkins-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/jenkins-archive-keyring.gpg] https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt-get install jenkins -y

# Install Docker
sudo apt install docker.io -y

# Add the current user to the Docker group to allow Jenkins to use Docker
sudo usermod -aG docker jenkins

# Install Python 3 and pip
sudo apt install python3-pip -y

# Install Virtualenv
sudo pip3 install virtualenv

# install aws cli
sudo apt install awscli -y

# Restart Jenkins service
sudo systemctl restart jenkins

# Instructions to install the Docker Pipeline plugin in Jenkins UI are missing
echo "Please log in to the Jenkins UI and install the Docker Pipeline plugin."


# Additional instructions or commands for setting up Docker Pipeline in Jenkins can be added here.
