import boto3
import botocore
Bucket_Name = input("enter the bucket name : ")
Object_Name = input("enter the Object name : " )
File_Name = input("enter a file name to save: ")
s3 = boto3.client("s3")
result = s3.download_file('%s'%(Bucket_Name),'%s'%(Object_Name),'%s'%(File_Name))
