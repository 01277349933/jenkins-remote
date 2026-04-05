# Task 2: Jenkins Remoting Project — CodeAlpha DevOps Internship

## 📌 Overview
This project demonstrates **Jenkins Remoting** — connecting remote Jenkins agents (nodes) to distribute build workloads across different machines and architectures. Builds run on remote Linux and Windows agents in parallel, with results collected on the master.

## 🛠️ Technologies Used
- Jenkins (Pipeline / Declarative)
- Jenkins Remoting (JNLP / SSH)
- Python
- Docker (optional agent)

## 📁 Project Structure
```
task2-jenkins-remote/
├── Jenkinsfile         # Declarative pipeline with multi-node execution
├── app.py              # Demo app that prints system info from the agent
├── node-setup.conf     # Guide for connecting remote Jenkins agents
└── README.md           # This file
```

## 🔄 Pipeline Stages

| Stage | Agent | Description |
|---|---|---|
| **Build on Linux Agent** | `linux-agent` | Runs app on remote Linux node |
| **Build on Windows Agent** | `windows-agent` | Runs app on remote Windows node |
| **Parallel Remote Execution** | `linux-agent x2` | Two tasks run in parallel on distributed agents |
| **Collect & Report** | `master` | Aggregates results back to master |

## 🚀 How Jenkins Remoting Works

```
Jenkins Master
    │
    ├──► linux-agent  (SSH / JNLP)  ──► runs build jobs
    │
    ├──► windows-agent (JNLP)        ──► runs build jobs
    │
    └──► master                      ──► collects results
```

## ⚙️ Setup Steps

### 1. Add a Remote Agent in Jenkins
- Go to: **Manage Jenkins → Nodes → New Node**
- Set name: `linux-agent`
- Launch method: `Launch agents via SSH`
- Add the agent's IP and SSH credentials

### 2. Label the node
In the node config, add the label: `linux-agent`

### 3. Run the Pipeline
- Create a new Pipeline job in Jenkins
- Point it to this repo / Jenkinsfile
- Click **Build Now**

## 🔐 Security: Node Isolation
- Each agent runs under its own OS user
- SSH keys are scoped to specific commands
- Credentials stored in Jenkins Credentials Plugin (never in code)
- Agent labels restrict which jobs run on which nodes

## 🏃 Run app.py locally
```bash
python3 app.py
```
