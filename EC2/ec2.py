"""
#Staring instances
import boto3
from botocore.exceptions import ClientError
list = ["i-017b9081aa53254bf","i-03522258883c76ded","i-05c1155a4289fe971","i-0b299a30cf4e6097a"]
ec2 = boto3.client("ec2")
for InstanceId in list:
    try:
        ec2.start_instances(InstanceIds=[InstanceId], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    response = ec2.start_instances(InstanceIds=[InstanceId], DryRun=False)
    print(response)
"""
"""
# Stopping instances
import boto3
from botocore.exceptions import ClientError
list = ["i-017b9081aa53254bf","i-03522258883c76ded","i-05c1155a4289fe971","i-0b299a30cf4e6097a"]
ec2 = boto3.client("ec2")
for InstanceId in list:
    try:
        ec2.stop_instances(InstanceIds=[InstanceId], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    response = ec2.stop_instances(InstanceIds=[InstanceId], DryRun=False)
    print("Success",response)
"""
# rebooting instances
import boto3
from botocore.exceptions import ClientError
list = ["i-017b9081aa53254bf","i-03522258883c76ded","i-05c1155a4289fe971","i-0b299a30cf4e6097a"]
ec2 = boto3.client("ec2")
for InstanceId in list:
    try:
        ec2.reboot_instances(InstanceIds=[InstanceId], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            print("You don't have permission to reboot instances.")
            raise

    response = ec2.reboot_instances(InstanceIds=[InstanceId], DryRun=False)
    print("Sucess",response)
