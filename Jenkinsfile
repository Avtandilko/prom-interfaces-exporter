pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                script {
                    openshift.withProject( 'dev' ) {
                        def bld = openshift.startBuild("pie")
                        bld.untilEach {
                          return it.object().status.phase == "Running"
                        }
                        bld.logs('-f') 
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

