# Task 4: VPC and Networking Configuration

##  Objective
Create a custom Virtual Private Cloud (VPC) with both public and private subnets, configure networking for internet access, and secure the environment using route tables, security groups, and network ACLs.



##  AWS Services Used

- Amazon VPC
- Subnets (Public & Private)
- Internet Gateway (IGW)
- NAT Gateway
- Route Tables
- Elastic IP
- Security Groups
- Network ACLs


##  Steps Performed

### 1. **Created a Custom VPC**
- Name: `devops-task4-vpc`
- CIDR block: `10.0.0.0/16`
- DNS Hostnames: Enabled

### 2. **Created Subnets**
- `devops-public-subnet-1a` → `10.0.1.0/24` (AZ: us-east-1a)
- `devops-private-subnet-1b` → `10.0.2.0/24` (AZ: us-east-1b)

### 3. **Internet Gateway (IGW) Setup**
- Created and attached IGW to the VPC
- Enabled internet access for public subnet

### 4. **NAT Gateway for Private Subnet**
- Allocated an Elastic IP
- Created a NAT Gateway in the public subnet
- Used it to route internet traffic from the private subnet

### 5. **Route Tables Configuration**
- Public Route Table:
  - `0.0.0.0/0` → IGW
  - Associated with public subnet
- Private Route Table:
  - `0.0.0.0/0` → NAT Gateway
  - Associated with private subnet

### 6. **Security Group Configuration**
- Inbound rules:
  - SSH (22) from My IP
  - HTTP (80) from `0.0.0.0/0`
- Outbound rules: allow all (default)

### 7. **(Optional) Network ACL Configuration**
- Allowed HTTP, SSH, and ephemeral ports
- Associated with both public and private subnets

---

##  Routing Overview

| Route Table         | Associated Subnet     | Route to Internet          |
|---------------------|------------------------|-----------------------------|
| Public Route Table  | Public Subnet (1a)     | Via IGW (0.0.0.0/0)         |
| Private Route Table | Private Subnet (1b)    | Via NAT Gateway (0.0.0.0/0) |


---

##  Status

-  VPC created and verified
-  Subnets distributed across AZs
-  Public subnet can access internet via IGW
-  Private subnet can access internet via NAT
-  Security groups and route tables verified
