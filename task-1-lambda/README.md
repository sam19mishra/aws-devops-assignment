# Task 1: Lambda Function Deployment

## Objective
Create and deploy an AWS Lambda function that reads data from an S3 bucket when a file is uploaded, processes the content, and logs it to CloudWatch.

---

## AWS Services Used
- AWS Lambda
- Amazon S3
- AWS IAM
- Amazon CloudWatch

---

## Steps Performed

1. Created an S3 bucket named `devops-lambda-input-bucket`.
2. Wrote a Python Lambda function to:
   - Extract file metadata (bucket name and key)
   - Read and log the file content
3. Created an IAM Role with:
   - `AmazonS3ReadOnlyAccess`
   - `AWSLambdaBasicExecutionRole`
4. Deployed the Lambda function manually via the AWS Console.
5. Configured the S3 bucket to trigger the Lambda on file upload.
6. Tested by uploading a `.txt` file to the bucket and checking CloudWatch logs.

---

## How to Deploy and Test

### 1. Deploy Lambda
- Paste the code from `lambda_function.py` into the Lambda console.
- Assign the IAM role: `LambdaS3ExecutionRole`.

### 2. Setup S3 Trigger
- Create or use an existing S3 bucket.
- Add a trigger to the Lambda for `PUT` events.

### 3. Upload a Test File
- Upload `test.txt` to the bucket.
- Go to CloudWatch → Log Groups → `/aws/lambda/ReadS3FileFunction`.

---



## 🖼️ Screenshots

1. **s3-bucket.png** – Created S3 bucket
2. **lambda-code.png** – Lambda function code in the AWS console
3. **lambda-trigger.png** – S3 trigger configured on Lambda
4. **test-file-upload.png** – Uploading file to the S3 bucket
5. **cloudwatch-logs.png** – Log output of the file content in CloudWatch

---

## ✅ Output Verification
- Lambda execution logs show the full content of the uploaded file.
- No errors in Lambda or CloudWatch.


