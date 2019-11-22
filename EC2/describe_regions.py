import boto3
ec2 = boto3.client("ec2")
response = ec2.describe_regions()
print('Regions:',response['Regions'])
response2 = ec2.describe_availability_zones()
print('Availability Zones:',response2['AvailabilityZones'])
