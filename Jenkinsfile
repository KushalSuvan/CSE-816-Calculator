pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { git branch: 'main', url: 'https://github.com/KushalSuvan/CSE-816-Calculator' }
        }
        stage('Test') {
            steps { sh 'python -m unittest discover -s tests' }
        }
        stage('Build Docker') {
            steps { sh 'docker build -t kushaljenamani/calcapp:latest .' }
        }
        stage('Push to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u kushaljenamani --password-stdin'
                    sh 'docker push kushaljenamani/calcapp:latest'
                }
            }
        }
        stage('Deploy via Ansible') {
            steps { sh 'ansible-playbook ansible-playbook.yml' }
        }
    }
}
