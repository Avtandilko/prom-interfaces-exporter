pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                script {
                    openshift.withProject( 'dev' ) {
                        echo "Hello from project ${openshift.project()} in cluster ${openshift.cluster()}"
                    }
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

