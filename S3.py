import json
import boto3


class S3:
    def __init__(self, bucket, aws_access_key_id, aws_secret_access_key, region_name):
        self.endpoint_url = 'http://s3.twcstorage.ru'
        self.bucket = bucket

        self.s3 = boto3.client(
            's3',
            endpoint_url=self.endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    def put(self, key, object):
        json_bytes = json.dumps(object).encode('utf-8')

        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=json_bytes,
            ContentType='application/json',
            ContentLength=len(json_bytes)
        )
