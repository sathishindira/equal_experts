pipeline {
    agent any

    stages {
        stage("login aws ecr"){
            steps {

            sh " aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 520186517569.dkr.ecr.us-east-1.amazonaws.com"
        }
        }
        stage('build docker image') {

            steps {
                sh " docker build -t equal-experts:latest ."
            }
            
        stage('push the images to the aws ecr')
            steps {
                scripts{
                    """
                    #bin/bash
                    
                    docker tag equal-experts:latest 520186517569.dkr.ecr.us-east-1.amazonaws.com/equal-experts:latest

                    docker push 520186517569.dkr.ecr.us-east-1.amazonaws.com/equal-experts:latest
                    """
            }
        }
        }
    }
}