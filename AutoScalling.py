'''
#creating launch configuration
import boto3
As = boto3.client('autoscaling')
response = As.create_launch_configuration(
    IamInstanceProfile = 'arn:aws:iam::809410142182:instance-profile/Webserver',
    ImageId='ami-04b9e92b5572fa0d1',
    InstanceType='t2.micro',
    LaunchConfigurationName='my-launch-config',
    SecurityGroups=[
        'sg-0054ec6d5bc67a753',
    ],
)

print(response)'''
"""# creating instance profile
import boto3
iam = boto3.client("iam")
response = iam.create_instance_profile(InstanceProfileName='Webserver')
print(response)"""
"""
#==>adding role to instace profile
import boto3
iam = boto3.client("iam")
response = iam.add_role_to_instance_profile(InstanceProfileName='webserver',RoleName='s3access')
print(response)"""

"""
# getting details of instanceprofile
import boto3
iam = boto3.resource("iam")
response = iam.InstanceProfile('webserver')
print(response.create_date)
print(response.roles)"""
"""
#creating auto scaling group attach with Targetgroup
import boto3
As = boto3.client('autoscaling')
response = As.create_auto_scaling_group(
    AutoScalingGroupName='my-auto-scaling-group',
    LaunchConfigurationName='my-launch-config',
    MaxSize=3,
    MinSize=1,
    TargetGroupARNs=['arn:aws:elasticloadbalancing:us-east-1:809410142182:targetgroup/sample-elb/6d1240837410ca42'],
    VPCZoneIdentifier='subnet-027ab31fb0eb898c6,subnet-032aae3d1354ac690',
)

print(response)
"""

"""#describing autoscaling group
import boto3
As = boto3.client("autoscaling")
response = As.describe_auto_scaling_groups(AutoScalingGroupNames=['my-auto-scaling-group'])
print(response)"""

#describing loadbalancer which are attached to autoscaling group
import boto3
As = boto3.client("autoscaling")
#response = As.describe_load_balancers(AutoScalingGroupName='my-auto-scaling-group')
#print(response)
update = As.update_auto_scaling_group(
    AutoScalingGroupName='my-auto-scaling-group',
    MaxSize=4,
    MinSize=2,
    NewInstancesProtectedFromScaleIn=True,
    HealthCheckGracePeriod=120
)
print(update)


