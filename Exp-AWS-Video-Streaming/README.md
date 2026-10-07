# AWS Video Streaming using S3 and CloudFront

## Aim

To create a video streaming service using **Amazon S3 and Amazon CloudFront**.

## Technologies Used

- Amazon S3
- Amazon CloudFront
- AWS Elemental MediaConvert
- AWS DRM

## Experiment Setup

In this experiment, a video is stored in a private **Amazon S3 bucket**. 
Amazon CloudFront is used to securely deliver the video to users through a CDN.

## Steps

### Step 1: Create an S3 Bucket

1. Login to the **AWS Management Console**.
2. Open **S3**.
3. Click **Create bucket**.
4. Enter a unique bucket name.
5. Select the required AWS Region.
6. Keep **Block all public access** enabled.
7. Enable **Bucket Versioning**.
8. Enable **Default Encryption** using SSE-S3.
9. Click **Create bucket**.
10. Open the bucket and upload a test `.mp4` video.

### Step 2: Create a CloudFront Distribution

1. Open the **CloudFront** console.
2. Click **Create distribution**.
3. Select the S3 bucket as the origin.
4. Select **Origin Access Control (OAC)**.
5. Create an OAC if required.
6. Set the Viewer Protocol Policy to:

```text
Redirect HTTP to HTTPS

7. Allow the following HTTP methods:

```text
GET, HEAD

8. Select CachingOptimized as the cache policy.
9. For this basic experiment, do not enable additional security protections.
10. Click Create distribution.

### Step 3: Update S3 Bucket Policy

1. Open the S3 bucket.
2. Go to the Permissions tab.
3. Find Bucket policy.
4. Click Edit.
5. Add the policy provided by CloudFront.
6. Save the changes.
This allows CloudFront to securely access the private video stored in S3.

### Step 4: Test Video Streaming

1. Open the CloudFront console.
2. Wait until the distribution is deployed.
3. Copy the Distribution domain name.
4. Add the uploaded video filename to the CloudFront URL.

Example:
https://your-cloudfront-domain/video.mp4

5. Open the URL in a browser.
6. The video should load through CloudFront.

## Result

The video stored in the private **Amazon S3 bucket** was successfully delivered through **Amazon CloudFront**.

## Conclusion

This experiment demonstrates how **Amazon S3 and Amazon CloudFront** can be used to create a secure and efficient cloud-based video streaming service.
