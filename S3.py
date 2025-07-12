import json
import boto3


def get_client(access_key, secret_access_key, region_name):
    return boto3.client('s3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key,
        region_name=region_name)


def push_object(client, bucket, key, object):
    try:
        client.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(object),
            ContentType='application/json'
        )
    except Exception as e:
        return str(e)
