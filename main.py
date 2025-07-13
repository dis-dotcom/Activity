import Secret
import LogActivityJob
import CompactActivityJob

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

#scheduler = BackgroundScheduler()
#scheduler.add_job(lambda: LogActivityJob.run(vk, s3), 'interval', minutes=1)
#scheduler.add_job(lambda: CompactActivityJob.run(s3), 'interval', minutes=1)
#scheduler.start()

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    return index_page


@app.get("/api/jobs/{job}/run")
async def job_run(job: str):
    if job == 'LogActivityJob':
        LogActivityJob.run(vk, s3)
    if job == 'CompactActivityJob':
        CompactActivityJob.run(s3)
