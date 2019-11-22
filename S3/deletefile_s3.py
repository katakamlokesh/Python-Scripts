import boto3
Bucket_Name = input("enter the bucket name : ")
File_Name = input("enter the filename : ")
s3 = boto3.client('s3')
s3.delete_object(Bucket='%s'%(Bucket_Name), Key='%s'%(File_Name))
