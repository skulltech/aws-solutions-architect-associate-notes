import boto3

#Create a table in default region 'users' with partition key, no sort key
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
        
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)


