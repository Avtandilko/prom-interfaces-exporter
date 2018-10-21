pipeline {
    agent any
    def appName="${NAME}"

    stages {
        stage('Build in dev environment') {
            steps {
                script {
                    openshift.withProject( 'dev' ) {
                        def bld = openshift.startBuild("${appName}"
                    }
                }
            }
        }
        stage('Run tests') {
            parallel {
                steps {
                    echo 'Test 1'
                }
                steps {
                    echo 'Test 2'
                }
            }
        }
    }
}

