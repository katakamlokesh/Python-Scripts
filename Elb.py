'''
# create target group
import boto3
from botocore.exceptions import ClientError
elb = boto3.client("elbv2")

response = elb.create_target_group(
    Name='sample-elb',
    Protocol='HTTP',
    Port=80,
    VpcId='vpc-06f4854d999226694',
    HealthCheckProtocol='HTTP',
    HealthCheckPort='traffic-port',
    HealthCheckEnabled=True,
    HealthCheckPath='/',
    HealthCheckIntervalSeconds=30,
    HealthCheckTimeoutSeconds=5,
    HealthyThresholdCount=5,
    UnhealthyThresholdCount=2,
    Matcher={'HttpCode': '404'},
    TargetType='instance'
)

print(response)
'''
'''
# describing target group attributes
import boto3
from botocore.exceptions import ClientError
elbv2 = boto3.client("elbv2")
response = elbv2.describe_target_group_attributes(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-east-1:809410142182:targetgroup/sample-elb/6d1240837410ca42'
)
print(response)'''
'''
# modify taget group
import boto3
from botocore.exceptions import ClientError
elbv2 = boto3.client("elbv2")

response = elbv2.modify_target_group(
    TargetGroupArn='arn:aws:elasticloadbalancing:us-east-1:809410142182:targetgroup/sample-elb/6d1240837410ca42',
    HealthCheckProtocol='HTTP',
    HealthCheckPort='traffic-port',
    HealthCheckEnabled=True,
    HealthCheckPath='/',
    HealthCheckIntervalSeconds=300,
    HealthCheckTimeoutSeconds=50,
    HealthyThresholdCount=10,
    UnhealthyThresholdCount=4,
    Matcher={'HttpCode': '204'}
)
print(response)
'''
"""
import boto3
elbv2 = boto3.client("elbv2")
response = elbv2.create_load_balancer(
    Name='myloadbalancer',
    Subnets=[
        'subnet-027ab31fb0eb898c6',
        'subnet-032aae3d1354ac690',
    ],
)
print(response)
"""
'''
# getting info of any load balancer
import boto3
lbarn = input("enter the load balancer arn: ")
elbv2 = boto3.client("elbv2")
response = elbv2.describe_load_balancer_attributes(
    LoadBalancerArn='%s'%lbarn
)
print(response)'''
"""
# modifying loadbalancer attributes
import boto3
lbarn = input("enter the load balancer arn: ")
elbv2 = boto3.client("elbv2")
response = elbv2.modify_load_balancer_attributes(
    Attributes=[
        {
            'Key': 'deletion_protection.enabled',
            'Value': 'true',
        },
    ],
    LoadBalancerArn='%s'%lbarn ,
)
print(response)"""

