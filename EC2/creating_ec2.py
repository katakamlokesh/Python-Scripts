import boto3
ec2 = boto3.client('ec2')
response = ec2.run_instances(ImageId='ami-04b9e92b5572fa0d1',InstanceType='t2.micro',KeyName='ec2-keypair',MinCount=1,MaxCount=1)
#for instance in response['Instances']:
#    print(Instance['InstanceId'])
