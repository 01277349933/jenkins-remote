// Jenkins Remoting Pipeline — CodeAlpha DevOps Internship Task 2
// Demonstrates distributing builds across multiple remote Jenkins agents

pipeline {

    // Use any available agent (master or remote node)
    agent none

    environment {
        APP_NAME    = 'jenkins-remote-demo'
        BUILD_DIR   = 'build'
    }

    stages {

        // ─────────────────────────────────────────────
        // Stage 1: Run on Remote Linux Agent
        // ─────────────────────────────────────────────
        stage('Build on Linux Agent') {
            agent {
                label 'linux-agent'   // Targets the remote Linux node
            }
            steps {
                echo "Running on remote Linux node: ${env.NODE_NAME}"
                echo "Workspace: ${env.WORKSPACE}"
                sh '''
                    echo "=== System Info ==="
                    uname -a
                    hostname
                    python3 --version
                    echo "=== Running App ==="
                    python3 app.py
                '''
            }
            post {
                success {
                    echo "Linux agent build PASSED on node: ${env.NODE_NAME}"
                }
                failure {
                    echo "Linux agent build FAILED"
                }
            }
        }

        // ─────────────────────────────────────────────
        // Stage 2: Run on Remote Windows Agent
        // ─────────────────────────────────────────────
        stage('Build on Windows Agent') {
            agent {
                label 'windows-agent'  // Targets the remote Windows node
            }
            steps {
                echo "Running on remote Windows node: ${env.NODE_NAME}"
                bat '''
                    echo === System Info ===
                    systeminfo | findstr /C:"OS Name"
                    echo === Running App ===
                    python app.py
                '''
            }
            post {
                success {
                    echo "Windows agent build PASSED on node: ${env.NODE_NAME}"
                }
                failure {
                    echo "Windows agent build FAILED (skipped if no Windows node)"
                }
            }
        }

        // ─────────────────────────────────────────────
        // Stage 3: Parallel Jobs on Multiple Agents
        // ─────────────────────────────────────────────
        stage('Parallel Remote Execution') {
            parallel {

                stage('Task on Agent-1') {
                    agent { label 'linux-agent' }
                    steps {
                        echo "Agent-1 (${env.NODE_NAME}): Running isolated task..."
                        sh 'sleep 2 && echo "Agent-1 done"'
                    }
                }

                stage('Task on Agent-2') {
                    agent { label 'linux-agent' }
                    steps {
                        echo "Agent-2 (${env.NODE_NAME}): Running isolated task in parallel..."
                        sh 'sleep 2 && echo "Agent-2 done"'
                    }
                }

            }
        }

        // ─────────────────────────────────────────────
        // Stage 4: Collect Results on Master
        // ─────────────────────────────────────────────
        stage('Collect & Report') {
            agent { label 'master' }
            steps {
                echo "All remote agents completed. Collecting results on master."
                sh '''
                    echo "Build ID   : ${BUILD_NUMBER}"
                    echo "App Name   : ${APP_NAME}"
                    echo "Status     : SUCCESS"
                    echo "Nodes used : linux-agent, windows-agent"
                '''
            }
        }

    }

    // ─────────────────────────────────────────────
    // Post-pipeline notifications
    // ─────────────────────────────────────────────
    post {
        success {
            echo "Pipeline completed successfully across all remote nodes!"
        }
        failure {
            echo "Pipeline failed. Check agent connectivity and node labels."
        }
        always {
            echo "Pipeline finished. Node: ${env.NODE_NAME ?: 'N/A'}"
        }
    }

}
