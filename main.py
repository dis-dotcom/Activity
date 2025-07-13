import json
import Secret
from S3 import S3
from VK import VK
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from DateTime import Now, Today, ToDateTime
from index import index as index_page
from apscheduler.schedulers.background import BackgroundScheduler


ids = Secret.get('ids').split(',')

vk = VK(
    Secret.get('token')
)

s3 = S3(
    Secret.get('s3_bucket_name'),
    Secret.get('s3_access_key'),
    Secret.get('s3_secret_access_key'),
    'ru-1'
)

scheduler = BackgroundScheduler()
scheduler.add_job(lambda: job(), 'interval', minutes=1)
scheduler.start()

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    return index_page


@app.get("/api/version")
async def version():
    return {'version': '0.0.0.2'}


@app.get("/api/objects")
async def log():
    return {'objects': s3.get_objects('')[:10]}


def job():
    try:
        print("Воркер запустился: " + Now())
        log_activity()
        print("Воркер завершился: " + Now())
    except Exception as ex:
        print("Воркер завершился с ошибкой: " + Now() + '\n' + str(ex))


def log_activity():
    for id in ids:
        user_info = vk.get_user_info(id)

        if 'response' in user_info.keys():
            if len(user_info['response']) > 0:
                first = user_info['response'][0]
                if 'last_seen' in first.keys():
                    user_info['last_activity'] = ToDateTime(first['last_seen']['time'], +3)
                if 'online' in first.keys():
                    user_info['online'] = str(first['online']) == '1'

        s3.put_async(
            key=f"{Today()}/{id}/{Now()}.json",
            object=user_info
        )


log_activity()
