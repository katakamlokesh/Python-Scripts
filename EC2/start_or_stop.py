import boto3
ec2 = boto3.client('ec2')
instance_id = input("enter the instances ids saperated by space :")
instance_list = instance_id.split()
for i in instance_list:
      try:
          response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
      except ClientError as e:
          print(e)
