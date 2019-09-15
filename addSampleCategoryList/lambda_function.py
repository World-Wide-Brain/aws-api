import json
import boto3
import uuid
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('samples')
def lambda_handler(event, context):
    try:
        if not event:
            return {'statusCode': 500, 'body': "empty event, please send data to save."}
        event.update( {'uuid' : str(uuid.uuid4())} )
        status = table.put_item(Item=event)
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': e.response['Error']['Message']+" event is = "+str(event)
        }
    else:
        return {
            'statusCode': 200,
            'body': status
        }