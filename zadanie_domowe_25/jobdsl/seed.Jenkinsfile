pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Generate jobs') {
            steps {
                jobDsl targets: 'zadanie_domowe_25/jobdsl/project_jobs.groovy',
                       removedJobAction: 'IGNORE',
                       removedViewAction: 'IGNORE',
                       lookupStrategy: 'JENKINS_ROOT'
            }
        }
    }
}
