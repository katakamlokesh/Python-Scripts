import boto3
username = input ("enter the username : ")
iam = boto3.client('iam')
iam.delete_user(UserName='%s'%(username))
