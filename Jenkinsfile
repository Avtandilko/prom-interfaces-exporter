pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                script {
                    openshift.withProject( 'dev' ) {
                        sh "oc create -f BuildConfig.yaml"
                        def bld = openshift.startBuild("pie")
                    }
                }
            }
        }
        stage('Run tests') {
            parallel {
                stage ('Run test 1') {
                    steps {
                        echo 'Test 1'
                    }
                }
                stage ('Run test 2') {
                    steps {
                        echo 'Test 2'
                    }
                }
            }
        }
    }
}

