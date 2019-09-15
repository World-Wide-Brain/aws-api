import json
import base64
import boto3
S3_BUCKET_NAME = 'wwb'
def lambda_handler(event, context):
    file_path = event['path']
    s3 = boto3.client('s3')
    try:
        s3_response = s3.get_object(Bucket=S3_BUCKET_NAME, Key=file_path)
        content = base64.b64encode(s3_response['Body'].read())
    except Exception as e:
        raise IOError(e)
    return {
        'statusCode': 200,
        'body': {
            'file_content': content.decode('utf-8')
        }
    }