pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        REPORT_DIR = 'reports'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aashima1-git/ci-tests.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    ${VENV_DIR}/bin/pip install --upgrade pip
                    ${VENV_DIR}/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Sanity Tests') {
            steps {
                sh '''
                    mkdir -p ${REPORT_DIR}
                    ${VENV_DIR}/bin/python -m pytest tests/test_sanity.py \
                    --html=${REPORT_DIR}/sanity_report.html --self-contained-html
                '''
            }
        }

        stage('Run Regression Tests') {
            steps {
                sh '''
                    mkdir -p ${REPORT_DIR}
                    ${VENV_DIR}/bin/python -m pytest tests/test_regression.py \
                    --html=${REPORT_DIR}/regression_report.html --self-contained-html
                '''
            }
        }

        stage('Publish Reports') {
            steps {
              sh '''  publishHTML([
                    reportDir: "${REPORT_DIR}",
                    reportFiles: 'sanity_report.html,regression_report.html',
                    reportName: 'Test Reports'
                ])
                '''
            }
        }
    }

    post {
        success {
            slackSend(channel: '#ci-pipeline', message: "✅ Build SUCCESS: ${env.JOB_NAME} [${env.BUILD_NUMBER}]")
           sh ''' emailext(
                subject: "✅ SUCCESS: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}",
                body: "Build succeeded.\nCheck Jenkins for reports.",
                to: "aashimabhardwaj18@gmail.com"
            ) 
            '''
        }
        failure {
            slackSend(channel: '#ci-pipeline', message: "❌ Build FAILED: ${env.JOB_NAME} [${env.BUILD_NUMBER}]")
           sh ''' emailext(
                subject: "❌ FAILURE: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}",
                body: "Build failed.\nCheck Jenkins logs.",
                to: "aashimabhardwaj18@gmail.com"
            )
            '''
        }
        always {
            archiveArtifacts artifacts: "${REPORT_DIR}/*.html", allowEmptyArchive: true
        }
    }
}
