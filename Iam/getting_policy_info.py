import boto3
policy_arn = input("enter the policy arn : ")
iam = boto3.client("iam")
policy = iam.get_policy(PolicyArn='%s'%(policy_arn))
print(policy['Policy'])
