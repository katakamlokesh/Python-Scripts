import boto3
Bucket = input('enter the bucket name : ')
s3 = boto3.client('s3')
result = s3.get_bucket_acl(Bucket='%s'%(Bucket))
print(result)
