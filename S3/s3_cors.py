import boto3
s3 = boto3.client("s3")
cors_configuration = {'CORSRules':[{'AllowedHeaders':['Authorization'],'AllowedMethods':['GET','PUT'],'AllowedOrigins':['*'],'ExposeHeaders':['GET','PUT'],'MaxAgeSeconds': 3000}]}
#result = s3.put_bucket_cors(Bucket='katakam-02',CORSConfiguration=cors_configuration)
#print(result)
response = s3.get_bucket_cors(Bucket='katakam-02')
print(response)
