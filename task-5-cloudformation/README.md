# Task 5: Infrastructure as Code with AWS CloudFormation

##  Objective
Define and deploy infrastructure using AWS CloudFormation. The stack includes:
- A custom VPC
- Public subnet
- Internet Gateway and route table
- Security Group for HTTP and SSH
- An EC2 instance configured to run a web server

---

##  AWS Services Used

- AWS CloudFormation
- Amazon EC2
- Amazon VPC (subnets, route tables, IGW)
- Amazon Security Groups

---

##  Steps Performed

### 1. **Created CloudFormation Template**
- File: `vpc-ec2-template.yaml`
- Resources defined:
  - VPC (`10.0.0.0/16`)
  - Public Subnet (`10.0.1.0/24`)
  - Internet Gateway and route table
  - Security Group for HTTP (80) and SSH (22)
  - EC2 instance (Amazon Linux 2, `t2.micro`)
  - UserData to install Apache and serve a sample webpage

### 2. **Deployed the Stack**
- Used AWS Console > CloudFormation > Create Stack
- Uploaded the YAML template
- Provided KeyPair name as parameter
- Stack name: `task5-stack`

### 3. **Validated Deployment**
- EC2 instance created in the public subnet
- HTTP access tested via browser
- Apache served HTML content:
