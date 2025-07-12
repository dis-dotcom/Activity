import json
import boto3
from botocore.client import Config


def get_client(access_key, secret_access_key):
    return boto3.client('s3',
        endpoint_url='https://s3.twcstorage.ru',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key,
        region_name='ru-1',
        config=Config(
            signature_version='s3v4',
            s3={'addressing_style': 'path'}
        )
    )


def push_object(client, bucket, key, object):
    try:
        client.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(object).encode('utf-8'),
            ContentType='application/json'
        )
    except Exception as e:
        return str(e)
