pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-username/ci-tests.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Sanity Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/test_sanity.py --html=reports/sanity_report.html --self-contained-html'
            }
        }

        stage('Run Regression Tests') {
            steps {
                sh '. venv/bin/activate && pytest tests/test_regression.py --html=reports/regression_report.html --self-contained-html'
            }
        }

        stage('Publish Reports') {
            steps {
                publishHTML([
                    reportDir: 'reports',
                    reportFiles: 'sanity_report.html,regression_report.html',
                    reportName: 'Test Reports'
                ])
            }
        }
    }

    post {
        success {
            slackSend(channel: '#ci-pipeline', message: "✅ Build SUCCESS: ${env.JOB_NAME} [${env.BUILD_NUMBER}]")
            emailext(
                subject: "✅ SUCCESS: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}",
                body: "Build succeeded.\nCheck Jenkins for reports.",
                to: "team@example.com"
            )
        }
        failure {
            slackSend(channel: '#ci-pipeline', message: "❌ Build FAILED: ${env.JOB_NAME} [${env.BUILD_NUMBER}]")
            emailext(
                subject: "❌ FAILURE: ${env.JOB_NAME} Build #${env.BUILD_NUMBER}",
                body: "Build failed.\nCheck Jenkins logs.",
                to: "team@example.com"
            )
        }
        always {
            archiveArtifacts artifacts: 'reports/*.html', allowEmptyArchive: true
        }
    }
}