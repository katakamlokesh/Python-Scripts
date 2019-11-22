import boto3
Bucket_Name=input("enter the bucket name : ")
web = { 
        'ErrorDocument':{'Key': 'error.html'}, 
        'IndexDocument':{'Suffix': 'index.html'},
}
s3 = boto3.client("s3")
result = s3.put_bucket_website(Bucket='%s'%(Bucket_Name),WebsiteConfiguration=web)
print(result)
