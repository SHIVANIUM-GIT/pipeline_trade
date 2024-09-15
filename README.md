# Pipeline Trade

This is a Python-based trading pipeline that utilizes the Fyers API for executing trades. The project follows DevOps best practices, including CI/CD pipeline implementation using Jenkins, cloud infrastructure setup via Terraform, monitoring using Prometheus and Grafana, and email notifications for alerts. The project securely handles credentials through environment variables stored in a `.env` file.

## Features

- **Trading API Integration**: Automated trades via the Fyers API.
- **Cloud Infrastructure**: Terraform used to deploy infrastructure for the trading pipeline on cloud providers (AWS, GCP, or Azure).
- **CI/CD Pipeline**: Jenkins automates continuous integration and deployment for automated code testing and deployment.
- **Monitoring**: Integrated Prometheus for metric collection and Grafana for real-time dashboard visualizations.
- **Alerts**: Configured Gmail SMTP for sending alerts in case of critical events in the pipeline.

## Requirements

- Python 3.x
- Fyers API v3
- `python-dotenv` for managing environment variables
- Jenkins for CI/CD pipeline automation
- Terraform for cloud infrastructure provisioning
- Prometheus for monitoring
- Grafana for visualization
- Gmail for alert notifications

## Installation

To set up the project, install the necessary dependencies by running the following commands:

```bash
pip install fyers-apiv3 python-dotenv
```

## Cloud Infrastructure Setup with Terraform

### 1. Terraform Setup
Terraform is used to provision the necessary cloud infrastructure (such as EC2 instances in AWS or VMs in GCP/Azure) to run the trading pipeline. Follow the steps below to set it up:

1. Install Terraform from the [official website](https://www.terraform.io/downloads).
2. Define your infrastructure in `main.tf`. Here's an example for an AWS EC2 instance:

   ```hcl
   module "security_group" {
    source = "./module/security_group"
    project_name =  project_name
   }
   ```

3. Initialize Terraform:
   ```bash
   terraform init
   ```

4. Apply the configuration to provision your cloud instance:
   ```bash
   terraform apply
   ```

5. Once the instance is provisioned, you can SSH into it and set up the trading pipeline.

### 2. Environment Variables
- Create a `.env` file in the root of your project directory.
- Add your Fyers API key, secret, and other credentials into this file:

   ```bash
   CLIENT_ID="your_fyers_client_id"
   SECRET_KEY="your_fyers_secret_key"
   REDIRECT_URI="your_url"
   USER_ID="your_fyers_user_id"
   PIN="your_account_pin"
   TOTP="your_totp_secret_key"
   ```

## CI/CD Pipeline with Jenkins

Jenkins is used to automate the continuous integration and deployment of the trading pipeline:

### 1. Jenkins Setup

1. Install Jenkins on your cloud instance using Terraform or manually by following the [official Jenkins installation guide](https://www.jenkins.io/doc/book/installing/).
2. Configure Jenkins to clone the trading pipeline repository from GitHub.
3. Create a new Jenkins pipeline job and set up the `Jenkinsfile`. Example pipeline steps:
   
   ```groovy
   pipeline {
       agent any
       stages {
           stage('Checkout') {
               steps {
                   git 'https://github.com/SHIVANIUM-GIT/pipeline_trade.git'
               }
           }
           stage('Install Dependencies') {
               steps {
                   sh 'pip install fyers-apiv3 python-dotenv'
               }
           }
           stage('Run Pipeline') {
               steps {
                   sh 'python fyersacceskey.py'
               }
           }
       }
   }
   ```

4. Trigger the pipeline automatically on code changes (set up GitHub webhook or use polling).

### 2. Deploy Trading Pipeline

1. After Jenkins completes the build, it will automatically deploy the trading pipeline to the cloud instance provisioned by Terraform.
2. This ensures continuous deployment whenever new changes are pushed to the repository.

## Monitoring and Alerts

- **Prometheus**: Monitors key system metrics such as CPU, memory usage, and API performance.
- **Grafana**: Visualizes metrics in customizable dashboards for real-time monitoring of your trading pipeline.
- **Gmail Alerts**: Sends critical alerts, such as API failures or system downtimes, via email using Gmail SMTP.

### 1. Gmail SMTP Setup for Alerts:
- Configure the Gmail SMTP server in your application to send email alerts for pipeline events:

   ```bash
   SMTP_SERVER="smtp.gmail.com"
   SMTP_PORT="587"
   SMTP_EMAIL="your_gmail_email"
   SMTP_PASSWORD="your_gmail_password"
   ```

## Usage

1. Make sure to activate your Python virtual environment (if using one) before running the pipeline.
2. Run your Python script as follows:

   ```bash
   python fyersacceskey.py
   ```

## Contributing

Feel free to submit pull requests or raise issues if you'd like to contribute to the project.
