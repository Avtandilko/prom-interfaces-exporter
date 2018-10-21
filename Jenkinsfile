pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                script {
                    openshift.create('https://github.com/Avtandilko/prom-interfaces-exporter.git')
                }
            }
        }
        stage('stage-2') {
            steps {
                echo 'Deploy'
            }
        }
    }
}

