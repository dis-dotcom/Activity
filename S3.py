import json
import boto3
import threading


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

    def get_objects(self, prefix):
        result = self.s3.list_objects_v2(
            Bucket=self.bucket,
            Prefix=prefix
        )

        return [] if 'Contents' not in result else result['Contents']

    def put_async(self, key, obj):
        threading.Thread(target=self.put, args=(key, obj)).start()

    def put(self, key, obj):
        json_bytes = json.dumps(obj).encode('utf-8')

        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=json_bytes,
            ContentType='application/json',
            ContentLength=len(json_bytes)
        )

    def get_string(self, key):
        response = self.s3.get_object(Bucket=self.bucket, Key=key)

        return response['Body'].read().decode('utf-8')

    def get_object(self, key):
        response = self.s3.get_object(Bucket=self.bucket, Key=key)

        return json.loads(response['Body'].read().decode('utf-8'))

    def delete_by_key(self, key):
        self.s3.delete_object(
            Bucket=self.bucket,
            Key=key
        )
