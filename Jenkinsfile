pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "siva08/python-app.latest"  // Corrected spelling for docker-compose
        TARGET_EC2_USER = "ubuntu"
        TARGET_EC2_HOST = "172.31.41.32"
        SSH_KEY_PATH = "~/.ssh/jenkins-ec2-key"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Sivarepo24/jenkins-docker'  // Provide the repository URL here
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage('Login to Docker') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }

        stage('Deploy to Ec2'){
            steps{
                sshagent(credentials:['ec2-ssh-credentials']){
                    sh'''
                    ssh -o StrictHostKeyChecking=no -i $ssh_key_path $TARGET_EC2_USER@$TARGET_EC2_HOST << 'EOF'
                    docker pull $DOCKER_IMAGE
                    docker stop my_container || true
                    docker rm -f my_container || true
                    docker run -d --name my_Container -p 80:5000 $DOCKER_IMAGE
                    EOF'''
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh "docker rmi $DOCKER_IMAGE"
                }
            }
        }
    }
}
