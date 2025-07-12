import os
import Secret
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from DateTime import Now
from index import index as index_page
from S3 import S3


s3_bucket_name = Secret.get('s3_bucket_name')
s3_access_key = Secret.get('s3_access_key')
s3_secret_access_key = Secret.get('s3_secret_access_key')

app = FastAPI()

s3 = S3(
    s3_bucket_name,
    s3_access_key,
    s3_secret_access_key,
    'ru-1'
)


@app.get("/", response_class=HTMLResponse)
async def index():
    log_activity()

    return index_page


@app.get("/api/version")
async def version():
    return {
        'version': '0.0.0.2'
    }


@app.get("/api/logs")
async def log():
    with open('/home/.log', 'r', encoding='utf-8') as file:
        content = [line.strip() for line in file.readlines()]

    return {
        'lines': content
    }


def log_activity():
    now = str(Now())
    line = now + '\n'

    error = push_object(s3, s3_bucket_name, now, {
        'activity': now
    })

    if error:
        raise Exception(error)

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.write(line)
