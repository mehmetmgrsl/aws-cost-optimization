Backup of volume -> Snapshot
 - Delete EC2 instance if it is not needed any more and forgot to delete volumes and snaphots

 S3 buckets. Then if you don't need those bucket if you forgot to delete them.

 EKS cluster to test sth but forgot to delete it.

 Stale resources. Created but forgot to delete it.

----------------------
If any stale resources are detected, the DevOps Engineer can receive notifications, such as:

- Hey, I have noticed that you have created an EBS volume, but it is not attached to any EC2 instances.
- Or, you have created a bunch of snapshots that are not attached to any volumes or EC2 instances.

Why don't you delete them?

----------------------

Lambda functions:
 - python (boto3)
 - to talk to AWS API

 - Call Lambda function once a week using CloudWatch.


### Some tools
1. AWS Trusted Advisor 

- It provides recommendations across multiple categories, including cost optimization and security.
- It has free tier which includes basic checks and paid version for the detailed one.


 ### Resources:
 - [AWS Cost Optimization - Abhishek Veeramalla](https://www.youtube.com/watch?v=OKYJCHHSWb4&t=1182s)
 - [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
