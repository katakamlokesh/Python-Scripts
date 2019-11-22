import json
import boto3
username=input("enter user name :")
iam = boto3.client("iam")
outfile = open('%s.credentials'%(username),'w+')
response = iam.create_user(UserName='%s' %(username))
#data= json.dumps(response)
data = str(response)
print(data)
outfile.write(data)
