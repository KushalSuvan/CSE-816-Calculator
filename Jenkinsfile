pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KushalSuvan/CSE-816-Calculator'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t kushaljenamani/calcapp:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-pass', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push kushaljenamani/calcapp:latest'
                }
            }
        }

        stage('Deploy via Ansible') {
            steps {
                sh '~/ansible-venv/bin/ansible-playbook ansible-playbook.yml'
            }
        }
    }
}
