import json
import boto3
Bucket_Name = input("enter the bucket name : ")

bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Sid':'Addperm',
                'Effect':'Allow',
                'Principal':'*',
                'Action':['s3:GetObject'],
                'Resource':'arn:aws:s3:::%s/*' %(Bucket_Name)
                }
            ]
        }

bucket_policy = json.dumps(bucket_policy)
s3 = boto3.client("s3")
s3.put_bucket_policy(Bucket='%s'%(Bucket_Name),Policy=bucket_policy)
