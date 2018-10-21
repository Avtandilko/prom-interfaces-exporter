pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                script {
                    openshift.withProject( 'dev' ) {
                        oc create -f BuildConfig.yaml
                        def bld = openshift.startBuild("pie")
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

