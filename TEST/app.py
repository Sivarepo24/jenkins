def hello():
    return "welcome to jenkins add webhook add email notification"

if __name__ == "__main__":
    print(hello())



# pipeline {
#     agent any

#     environment {
#         DOCKER_IMAGE = "siva08/docker-compose"  // Corrected spelling for docker-compose
#     }

#     stages {
#         stage('Checkout Code') {
#             steps {
#                 git branch: 'main', url: 'https://github.com/Sivarepo24/jenkins-docker'  // Provide the repository URL here
#             }
#         }

#         stage('Build Docker Image') {
#             steps {
#                 script {
#                     sh "docker build -t $DOCKER_IMAGE ."
#                 }
#             }
#         }

#         stage('Login to Docker') {
#             steps {
#                 withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
#                     script {
#                         sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
#                     }
#                 }
#             }
#         }

#         stage('Push to DockerHub') {
#             steps {
#                 script {
#                     sh "docker push $DOCKER_IMAGE"
#                 }
#             }
#         }

#         stage('Cleanup') {
#             steps {
#                 script {
#                     sh "docker rmi $DOCKER_IMAGE"
#                 }
#             }
#         }
#     }
# }
