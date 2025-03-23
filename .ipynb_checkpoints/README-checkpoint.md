# 📲 SMS Spam Classifier – End-to-End MLOps on AWS SageMaker 🚀

A production-ready, fully automated machine learning pipeline for SMS spam detection using AWS SageMaker, Terraform, GitHub Actions CI/CD, monitoring, and advanced code security scanning.

---

## 📦 Project Overview

| Feature                  | Description                                                       |
|--------------------------|-------------------------------------------------------------------|
| 🧠 Model                 | TF-IDF + XGBoost (≥ 97% Accuracy)                                 |
| ⚙️ Pipeline              | Preprocessing → Training → Evaluation → Model Registry            |
| ☁️ Infra                 | Modular Terraform: A/B Testing, Canary Deployments, Monitoring     |
| 🚀 Deployment            | Automated via GitHub Actions + Terraform                          |
| 📊 Monitoring            | CloudWatch Alarms + Lambda traffic adjustment                     |
| 🔐 Security              | CodeQL + Snyk scanning + GitHub Secrets                           |
| 🧪 SageMaker AutoPilot   | Alternative AutoML baseline for model comparison                   |

---

## 🗂️ Folder Structure

sms-spam-mlops/
├── data/                        # 📁 Raw & processed data
│   ├── sms.tsv                  # 📄 Original dataset
│   └── processed/              # 📁 Cleaned or feature-engineered datasets
│       └── ...
│
├── notebooks/                  # 📒 Jupyter notebooks for dev, experimentation
│   ├── 01_train_and_eval.ipynb # 📘 Model training and evaluation
│   ├── 02_ab_testing.ipynb     # 📗 A/B testing implementation
│   └── 03_monitor_canary.ipynb # 📙 Monitoring (e.g., canary deployment, alarms)
│
├── inference/                  # 📁 Real-time inference scripts
│   └── tfidf_inference.py      # 📄 Inference handler (TF-IDF + model)
│
├── scripts/                    # 📁 Python scripts for local + SageMaker pipeline
│   ├── preprocess.py           # 📄 Local preprocessing
│   ├── sagemaker_preprocess.py# 📄 SageMaker preprocessing entry point
│   └── sagemaker_train.py      # 📄 SageMaker training script
│
├── pipelines/                  # 📁 ML pipeline orchestration (SageMaker Pipeline SDK)
│   └── sms_pipeline.py         # 📄 Pipeline definition
│
├── terraform/                  # 📁 Infrastructure-as-Code for automation
│   ├── main.tf                 # 📄 Terraform entry file
│   ├── ab_testing.tf           # 📄 A/B test resources (SageMaker, endpoints)
│   ├── cloudwatch.tf           # 📄 CloudWatch metrics + alarms
│   ├── lambda.tf               # 📄 Lambda functions for traffic shifting
│   ├── variables.tf            # 📄 Terraform variables
│   └── outputs.tf              # 📄 Terraform outputs
│
├── lambda/                     # 📁 AWS Lambda function code
│   └── lambda_canary_shift.py # 📄 Canary traffic shift logic
│
├── autopilot/                  # 📁 SageMaker Autopilot usage (AutoML)
│   └── autopilot_launcher.ipynb # 📒 Notebook to launch and evaluate Autopilot job
│
├── cicd/                       # 📁 CI/CD related config/scripts
│   └── github-actions.yml      # 📄 Unified GitHub Actions pipeline
│
├── .github/
│   └── workflows/              # 📁 GitHub Actions workflows
│       ├── deploy.yml          # 🚀 CI/CD deployment workflow
│       └── code-scan.yml       # 🛡️ Static code scanning workflow (e.g., CodeQL)
│
├── security/                   # 📁 Security & compliance configs
│   └── code_scan_config.yml    # 📄 Custom configuration for secure code scanning
│
└── README.md                   # 📘 Project overview, setup, and usage


---

## 🛠️ MLOps Workflow

### Phase 1: 🧹 Preprocessing (TF-IDF + Label Encoding)
- Clean text data
- Save `vectorizer.pkl`, `X_train.npy`, etc.

### Phase 2: 🧠 Model Training (XGBoost)
- Target Accuracy ≥ **97%**
- ROC, Confusion Matrix, Precision, Recall

### Phase 3: 🔁 SageMaker Pipelines
- `SKLearnProcessor` + `XGBoost` + Model Registry

### Phase 4: ☁️ Terraform Infra
- A/B EndpointConfig (90/10 split)
- Canary via CloudWatch + Lambda
- AutoPilot launch notebook

### Phase 5: 🚀 CI/CD Automation
- GitHub Actions deploy models + Terraform
- Notifications on failure/success

### Phase 6: 🔍 Monitoring
- CloudWatch Alarms for latency + accuracy
- Lambda rebalances traffic automatically

### Phase 7: 🔐 Code Scanning
- GitHub CodeQL
- Snyk Open Source Vulnerability Scanning

---

## 🚦 A/B + Canary Deployment

- **Model A (v1):** Stable Production
- **Model B (v2):** Canary 10%
- ⚠️ If `accuracy < 90%` or `latency > 3s`, Canary is scaled back or paused via Lambda

---

## 🧪 SageMaker AutoPilot (Optional)

Quickly launch and evaluate models from `autopilot/autopilot_launcher.ipynb` for:
- Baseline benchmarking
- Auto feature engineering
- Model comparison

---

## 🔐 Security & Quality

| Tool    | Coverage                      |
|---------|-------------------------------|
| ✅ CodeQL | Static code analysis          |
| ✅ Snyk   | Python dependency scanning    |
| ✅ Black  | Linting (PEP-8)               |
| ✅ Secrets | GitHub Actions Secret Store  |

---

## 🚀 CI/CD Workflow

1. **Push to `main` branch**
2. ✅ Run Preprocessing
3. ✅ Upload Artifacts to S3
4. ✅ Terraform Apply
5. ✅ Deploy Model + Endpoint
6. ✅ Monitor → Auto Traffic Shift

---

## 🧠 Skills Showcased

- **MLOps Engineering**
- **AWS SageMaker Pipelines**
- **Terraform Infra-as-Code**
- **GitHub Actions Automation**
- **CloudWatch + Lambda Triggers**
- **SageMaker AutoPilot / Model Registry**
- **CI/CD + Security (CodeQL, Snyk)**

---

## 📧 Contact

👤 Built by: *[Maduabighichi Achilefu]*  
📧 Email: [ask]  
🔗 LinkedIn: [linkedin.com/in/maduabughichiachilefu]

---

> ⭐️ *This project demonstrates real-world, production-grade MLOps practices — ideal for showcasing to hiring managers, MLOps teams, or cloud architecture roles.*
![CI/CD](https://img.shields.io/github/actions/workflow/status/maduoma/sms-spam-mlops/deploy.yml?label=CI%2FCD&style=flat-square&logo=github)
![Terraform](https://img.shields.io/badge/Terraform-Infra-blueviolet?logo=terraform&style=flat-square)
![AWS SageMaker](https://img.shields.io/badge/SageMaker-Deployed-green?logo=amazon-aws&style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python)
![Security Scan](https://img.shields.io/badge/Security-CodeQL%20%2B%20Snyk-critical?style=flat-square&logo=github)
