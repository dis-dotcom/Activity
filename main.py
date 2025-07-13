import Secret
import LogActivityJob

from S3 import S3
from VK import VK
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from index import index as index_page
from apscheduler.schedulers.background import BackgroundScheduler


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
scheduler.add_job(lambda: LogActivityJob.run(vk, s3), 'interval', minutes=1)
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


LogActivityJob.run(vk, s3)
