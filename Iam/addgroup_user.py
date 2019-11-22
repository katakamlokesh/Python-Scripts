Group_Name = input("enter tyhe group name : ")
User_Name = input("enter the user name : ")
import boto3
iam = boto3.client("iam")
response = iam.add_user_to_group(GroupName='%s'%(Group_Name),UserName='%s'%(User_Name))
print(response)
