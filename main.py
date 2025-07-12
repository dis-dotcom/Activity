import Secret
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from DateTime import Now
from index import index as index_page
from S3 import S3
from apscheduler.schedulers.background import BackgroundScheduler

s3_bucket_name = Secret.get('s3_bucket_name')
s3_access_key = Secret.get('s3_access_key')
s3_secret_access_key = Secret.get('s3_secret_access_key')

app = FastAPI()

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    return index_page


@app.get("/api/version")
async def version():
    return {'version': '0.0.0.2'}


@app.get("/api/logs")
async def log():
    with open('/home/.log', 'r', encoding='utf-8') as file:
        content = [line.strip() for line in file.readlines()]

    return {'lines': content}


def job():
    try:
        print("Воркер запустился: " + str(Now()))
        log_activity()
        print("Воркер завершился: " + str(Now()))
    except Exception as ex:
        print(str(ex))


def log_activity():
    now = str(Now())
    s3.put_async(now, {'activity': now})

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.write(now + '\n')


scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', minutes=1)
