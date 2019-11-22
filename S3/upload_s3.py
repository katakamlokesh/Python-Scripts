import boto3
filename = input("enter the file name: ")
Bucket = input("enter bucketname : ")
Object_Name = input("enter the Objectname : ")
s3 = boto3.client('s3')
s3.upload_file('%s'%(filename) ,'%s'%(Bucket),'%s'%(Object_Name))

