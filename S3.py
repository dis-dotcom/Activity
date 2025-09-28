import json
import boto3
import threading
from Logger import Logger


class S3:
    def __init__(self, settings):
        self.endpoint_url = 'http://s3.twcstorage.ru'
        self.bucket = settings['s3']['bucket']

        self.s3 = boto3.client(
            's3',
            endpoint_url=self.endpoint_url,
            aws_access_key_id=settings['s3']['access_key'],
            aws_secret_access_key=settings['s3']['secret_access_key'],
            region_name=settings['s3']['region_name']
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

        Logger.info(f'Создан файл {key}')

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
