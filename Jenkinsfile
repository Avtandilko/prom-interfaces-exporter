pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                openshiftBuild(namespace: 'dev', bldCfg: 'pie', showBuildLogs: 'true')
            }
        }
        stage('Deploy to dev environment') {
            steps {
                openshiftDeploy(namespace: 'dev', depCfg: 'pie')
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
