# Task 2: CI/CD Pipeline for a Web Application

## Objective
To build and deploy a simple static web application (HTML, CSS, JS) to an S3 bucket using AWS CI/CD services including CodePipeline and CodeBuild.

---

## AWS Services Used
- Amazon S3 (for static hosting)
- AWS CodePipeline
- AWS CodeBuild
- AWS IAM
- GitHub (source repo)

---

## Steps Performed

1. **Created a Simple Static Website**
   - Files: `index.html`, `styles.css`, `app.js`
   - Project pushed to a private GitHub repository

2. **Configured S3 for Static Hosting**
   - Created an S3 bucket: `devops-static-web-[yourname]`
   - Enabled static website hosting and public read access

3. **Wrote `buildspec.yml`**
   - Defines build and deployment artifacts for CodeBuild

4. **Created CodeBuild Project**
   - Connected to GitHub repo
   - Used `buildspec.yml` to process and prepare files
   - Output artifacts directed to S3 bucket

5. **Created CodePipeline**
   - Automatically triggered by commits to GitHub
   - Stages:
     - Source: GitHub
     - Build: CodeBuild
     - Deploy: S3

6. **Tested the Pipeline**
   - Triggered by pushing to GitHub
   - Verified

##  How to Deploy

### 1. Push Web Files to GitHub
Ensure files like `index.html`, `styles.css`, `buildspec.yml` are committed to `main`.

### 2. S3 Bucket Setup
- Enable **static website hosting**
- Add **public bucket policy** to allow access

### 3. Create CodeBuild Project
- Source: GitHub
- Environment: Ubuntu with `buildspec.yml`
- Output: S3 (static site bucket)

### 4. Create CodePipeline
- Connect source: GitHub
- Add build stage using the CodeBuild project
- Set deploy stage to S3 bucket