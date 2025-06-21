# AWS DevOps Engineer Assessment – Project Submission

##  Overview

This project is a comprehensive AWS DevOps Engineer assessment designed to demonstrate my proficiency in core AWS services, DevOps practices, and Infrastructure as Code. The implementation includes Lambda integrations, CI/CD automation, EC2 configuration, VPC design, CloudFormation templates, and monitoring solutions.

---

##  Repository Structure
aws-devops-assignment/
├── task-1-lambda/ # Lambda function triggered by S3
├── task-2-cicd/ # CI/CD pipeline deploying to S3
├── task-3-ec2/ # EC2 instance with Apache server
├── task-4-vpc/ # VPC and networking setup
├── task-5-cloudformation/ # Infra via CloudFormation template
├── task-6-monitoring/ # Monitoring & logging via CloudWatch
└── presentation/ # Presentation video/slides


---

##  Task Breakdown

###  Task 1: Lambda Function Deployment
- Wrote a Python Lambda function to read S3 files
- Configured trigger on S3 PUT
- Logs sent to CloudWatch

 [`task-1-lambda/`](./task-1-lambda/)

---

###  Task 2: CI/CD Pipeline for Web App
- Built a static web app (HTML/CSS/JS)
- Created a CodePipeline with CodeBuild to auto-deploy to S3
- Enabled public static hosting

 [`task-2-cicd/`](./task-2-cicd/)

---
###  Task 3: EC2 Instance Setup
- Launched Amazon Linux 2 EC2 instance
- Installed Apache via UserData
- Hosted a test web page
- Enabled CloudWatch agent for custom metrics

 [`task-3-ec2/`](./task-3-ec2/)

---

###  Task 4: VPC and Networking
- Created custom VPC with public and private subnets
- Set up IGW, NAT Gateway, route tables
- Secured with security groups and optional NACLs

 [`task-4-vpc/`](./task-4-vpc/)

---

###  Task 5: CloudFormation Template
- Created a YAML template to define and deploy:
  - VPC, subnet, route table, IGW
  - EC2 instance with web server
- Parameterized with KeyPair input

 [`task-5-cloudformation/`](./task-5-cloudformation/)

---

###  Task 6: Monitoring and Logging
- Enabled CloudWatch Logs for Lambda
- Installed CloudWatch Agent on EC2
- Created alarms for CPU usage and Lambda duration
- Set log retention to 7 days

 [`task-6-monitoring/`](./task-6-monitoring/)


---

## Details

Sameer Kumar
DevOps/Cloud Engineer  
 sam19mishra@gmail.com  
 +91 8709804562  
 LinkedIn: https://www.linkedin.com/in/sameerkumarcse/

---

##  Notes

- All resources were created and tested in the `ap-south-1` (Mumbai) region.
- Only AWS Free Tier resources were used where possible.




