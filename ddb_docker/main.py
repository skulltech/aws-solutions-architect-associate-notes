import os
import boto3

#os.environ['AWS_PROFILE'] = "default"
#os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

# For a Boto3 service resource ('resource' is for higher-level, abstracted access to Dynamo)
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

table = dynamodb.Table('Movies')
response = table.get_item(Key={'year': 2015, 'title': 'The Big New Movie'})

print (response)
print ('end response')
print(list(dynamodb.tables.all()))


print("Hello ending...")

#coming up?