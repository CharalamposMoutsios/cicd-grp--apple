# Use the official Jenkins LTS image as a base image
FROM jenkins/jenkins:lts

# Switch to root user to install packages
USER root

# Install Docker prerequisites
RUN apt-get update && \
    apt-get install -y apt-transport-https \
                       ca-certificates \
                       curl \
                       gnupg2 \
                       software-properties-common

# Add Docker GPG key
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

# Add Docker repository
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

# Install Docker
RUN apt-get update && \
    apt-get install -y docker-ce docker-ce-cli containerd.io

RUN apt-get install -y python3 python3-pip python3.11-venv

# Adding jenkins to docker group
RUN usermod -aG docker jenkins

# Switch back to the jenkins user
USER jenkins

# Set Jenkins configurations
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yaml

# Copy and install Jenkins plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt

# Copy Jenkins configuration as code
COPY casc.yaml /var/jenkins_home/casc.yaml
