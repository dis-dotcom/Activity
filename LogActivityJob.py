from S3 import S3
from VK import VK
from Secret import get
from DateTime import Now, Today, ToDateTime


def run(vk: VK, s3: S3):
    try:
        now = Now()
        print(f"Воркер запустился: {now}")
        [log_activity(now, x, vk, s3) for x in get('ids', ',')]
        print(f"Воркер завершился: " + Now())
    except Exception as ex:
        print(f"Воркер завершился с ошибкой: {Now()}" + '\n' + str(ex))


def log_activity(now, x: str, vk: VK, s3: S3):
    today = Today()
    user_info = vk.get_user_info(x)

    try:
        ticks = user_info['response'][0]['last_seen']['time']
        user_info['last_activity'] = ToDateTime(utc=+3, ticks=ticks)
    except Exception as ex:
        print(ex)

    try:
        online = str(user_info['response'][0]['online']) == '1'
        user_info['online'] = online
    except Exception as ex:
        print(ex)

    s3.put_async(
        key=f"{today}/{x}/{now}.json",
        object=user_info
    )