import boto3 
user_name = input("enter the username : ")
outfile = open('%s.Accesskeys'%(user_name),'w+')
iam = boto3.client("iam")
response = iam.create_access_key(UserName='%s'%(user_name))
print(response)
outfile.write(str(response))
