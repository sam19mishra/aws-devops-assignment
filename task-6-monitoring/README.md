# Task 6: Monitoring and Logging

##  Objective
Configure monitoring and logging for both EC2 and Lambda using Amazon CloudWatch. Ensure logs are retained for at least 7 days and set up alarms for critical thresholds.

---

##  AWS Services Used

- Amazon CloudWatch (Logs, Metrics, Alarms)
- AWS Lambda
- Amazon EC2
- IAM Roles and Policies

---

## Steps Performed

### 🔹 1. **Lambda Monitoring and Logging**

- CloudWatch logs automatically created by Lambda
- Verified logs in: `/aws/lambda/ReadS3FileFunction`
- Created alarm to monitor:
  - **Lambda Duration > 3 seconds**

**Alarm Setup:**
- Metric: `Duration`
- Threshold: > 3000 ms
- Period: 1 minute
- Alarm name: `LambdaDurationAlarm`

---

###  2. **EC2 Monitoring and Logging**

#### Installed and Configured CloudWatch Agent:

```bash
sudo yum install -y amazon-cloudwatch-agent
