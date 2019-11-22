import boto3
User_Name = input("enterthe username : ")
Password = input("enter user password : ")
iam = boto3.client("iam")
response = iam.create_login_profile(UserName='%s'%(User_Name),Password='%s'%(Password),PasswordResetRequired=True)
