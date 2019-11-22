import boto3 
ec2 = boto3.client('ec2')
resourse = ec2.terminate_instances(InstanceIds=['i-0f5227021720c7ac5'])
