import boto3
iam = boto3.client("iam")
response = iam.attach_user_policy(PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole',UserName='rakesh001')
print(response)

