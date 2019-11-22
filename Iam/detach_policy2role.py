import boto3
policy_arn=input('enter the policy arn : ')
Role_Name=input('enter the Role name : ')
iam = boto3.client("iam")
response = iam.detach_role_policy(PolicyArn='%s'%(policy_arn),RoleName='%s'%(Role_Name))
print(response)

