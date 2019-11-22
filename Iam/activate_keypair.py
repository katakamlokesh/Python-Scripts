import boto3
user_name = input("enter the user name : ")
id = input("enter the accesskey id : ")
secret = input("enter the secret access key id : ")
iam = boto3.resource('iam')
access_key_pair = iam.AccessKeyPair('%s'%(user_name),'%s'%(id),'%s'%(secret))
response = access_key_pair.activate()
print(response)
