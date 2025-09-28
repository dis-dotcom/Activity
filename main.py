import DateTime
import Secret
import LogActivityJob

from S3 import S3
from VK import VK
from fastapi import FastAPI
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


@app.get("/")
def index():
    return {"now": DateTime.Now()}

