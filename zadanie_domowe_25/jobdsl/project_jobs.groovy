folder('generated-jobs') {
    description('Folder wygenerowany przez Job DSL')
}

folder('generated-jobs/project-cicd') {
    description('Zadania CI/CD dla projektu generowane automatycznie przez Job DSL')
}

pipelineJob('generated-jobs/project-cicd/build-develop') {
    description('Build i test dla gałęzi develop')

    parameters {
        stringParam('APP_VERSION', '1.0.0', 'Wersja aplikacji')
        booleanParam('RUN_TESTS', true, 'Czy uruchomić testy')
    }

    triggers {
        scm('H/5 * * * *')
    }

    definition {
        cps {
            script("""
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'develop', url: 'https://github.com/PawelRa/cwiczenia-devops.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Build dla develop, wersja: \${APP_VERSION}"'
            }
        }

        stage('Test') {
            when {
                expression { params.RUN_TESTS }
            }
            steps {
                sh 'echo "Testy dla develop"'
                sh 'mkdir -p reports && echo "<testsuite></testsuite>" > reports/junit.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true
        }
    }
}
""")
            sandbox(true)
        }
    }
}

pipelineJob('generated-jobs/project-cicd/build-master') {
    description('Build i test dla gałęzi master')

    parameters {
        stringParam('APP_VERSION', '1.0.0', 'Wersja aplikacji')
        booleanParam('RUN_TESTS', true, 'Czy uruchomić testy')
    }

    triggers {
        scm('H/10 * * * *')
    }

    definition {
        cps {
            script("""
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/PawelRa/cwiczenia-devops.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Build dla master, wersja: \${APP_VERSION}"'
            }
        }

        stage('Test') {
            when {
                expression { params.RUN_TESTS }
            }
            steps {
                sh 'echo "Testy dla master"'
                sh 'mkdir -p reports && echo "<testsuite></testsuite>" > reports/junit.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true
        }
    }
}
""")
            sandbox(true)
        }
    }
}

pipelineJob('generated-jobs/project-cicd/build-feature') {
    description('Build i test dla gałęzi feature')

    parameters {
        stringParam('FEATURE_BRANCH', 'feature/przyklad', 'Nazwa gałęzi feature')
        stringParam('APP_VERSION', '1.0.0', 'Wersja aplikacji')
        booleanParam('RUN_TESTS', true, 'Czy uruchomić testy')
    }

    triggers {
        scm('H/15 * * * *')
    }

    definition {
        cps {
            script("""
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: params.FEATURE_BRANCH, url: 'https://github.com/PawelRa/cwiczenia-devops.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Build dla feature branch: \${FEATURE_BRANCH}, wersja: \${APP_VERSION}"'
            }
        }

        stage('Test') {
            when {
                expression { params.RUN_TESTS }
            }
            steps {
                sh 'echo "Testy dla feature branch: \${FEATURE_BRANCH}"'
                sh 'mkdir -p reports && echo "<testsuite></testsuite>" > reports/junit.xml'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*', allowEmptyArchive: true
        }
    }
}
""")
            sandbox(true)
        }
    }
}

pipelineJob('generated-jobs/project-cicd/deploy-test') {
    description('Wdrożenie na środowisko testowe')

    parameters {
        stringParam('APP_VERSION', '1.0.0', 'Wersja aplikacji')
        choiceParam('TARGET_ENV', ['test'], 'Środowisko docelowe')
        booleanParam('FORCE_DEPLOY', false, 'Wymuś wdrożenie')
    }

    triggers {
        cron('H 2 * * *')
    }

    definition {
        cps {
            script("""
pipeline {
    agent any

    stages {
        stage('Deploy to test') {
            steps {
                sh 'echo "Wdrożenie wersji \${APP_VERSION} na środowisko \${TARGET_ENV}"'
            }
        }
    }

    post {
        always {
            echo 'Zakończono deploy na test'
        }
    }
}
""")
            sandbox(true)
        }
    }
}

pipelineJob('generated-jobs/project-cicd/deploy-prod') {
    description('Wdrożenie na środowisko produkcyjne z ręcznym zatwierdzeniem')

    parameters {
        stringParam('APP_VERSION', '1.0.0', 'Wersja aplikacji')
        choiceParam('TARGET_ENV', ['prod'], 'Środowisko docelowe')
        booleanParam('FORCE_DEPLOY', false, 'Wymuś wdrożenie')
    }

    definition {
        cps {
            script("""
pipeline {
    agent any

    stages {
        stage('Approval') {
            steps {
                input message: 'Czy na pewno wdrożyć na produkcję?', ok: 'Wdróż'
            }
        }

        stage('Deploy to prod') {
            steps {
                sh 'echo "Wdrożenie wersji \${APP_VERSION} na środowisko \${TARGET_ENV}"'
            }
        }
    }

    post {
        always {
            echo 'Zakończono deploy na produkcję'
        }
    }
}
""")
            sandbox(true)
        }
    }
}
