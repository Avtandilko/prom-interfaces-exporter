pipeline {
    agent any

    stages {
        stage('Build in dev environment') {
            steps {
                script {
                    openshift.withProject( 'dev' ) {
                        def pie = openshift.newApp( 'https://github.com/Avtandilko/prom-interfaces-exporter.git' )
                        pie.describe()
                        //def bc = pie.narrow( 'bc' )
                        //def buildSelector = bc.startBuild()
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

