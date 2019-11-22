import boto3
import json 

Resource_Name = input("enter the user arn name : ")

policy = {
		"Version": "2012-10-17",
		"Statement": [
		    {
			"Effect": "Allow",
			"Action": "s3:*",
			"Resource": "%s"%(Resource_Name)
		     }
	     	]
	  }
iam = boto3.client("iam")
response = iam.create_policy(PolicyName='AmazonS3FullAccess',PolicyDocument=json.dumps(policy))
print(response)
