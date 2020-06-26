import os
import boto3
from decimal import Decimal

#os.environ['AWS_PROFILE'] = "default"
#os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

# For a Boto3 service resource ('resource' is for higher-level, abstracted access to Dynamo)
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

#set table to Movies table and get item with key=2015
#table = dynamodb.Table('Movies')
#response = table.get_item(Key={'year': 2015, 'title': 'The Big New Movie'})


#set table to Users table key='id' N and create/put item
# table = dynamodb.Table('users')
# response = table.put_item(
#        Item={
#             'id': 1,
#             'name': 'kwaku',
#             'surname':'tee',
#             'age':10
#         }
#     )



#set table to users table and update id=1 age atomic counter increment +1
table = dynamodb.Table('users')
response1 = table.update_item(
        Key={
            'id': 1
            },
        UpdateExpression="set age= age + :a",
        ExpressionAttributeValues={
            ':a': Decimal(1)
        },
        ReturnValues="UPDATED_NEW"
    )

print("printing response1")
print(response1)

#set table to users table and read
#table = dynamodb.Table('users')
response = table.get_item(Key={'id': 1})

print (response['Item'])
print ('end response')
print(list(dynamodb.tables.all()))


print("Hello ending...")

#end