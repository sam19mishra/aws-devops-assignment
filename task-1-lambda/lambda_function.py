import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Get bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Read the object content
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    print(f"File content from {key}:")
    print(content)
    
    return {
        'statusCode': 200,
        'body': json.dumps('File processed successfully!')
    }
