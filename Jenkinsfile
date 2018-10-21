pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                openshiftBuild(namespace: 'dev', buildConfig: 'pie', showBuildLogs: 'true')
            }
        }
        stage('Deploy to dev environment') {
            steps {
                openshiftDeploy(namespace: 'dev', deploymentConfig: 'pie')
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
