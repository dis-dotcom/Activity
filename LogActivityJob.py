from S3 import S3
from VK import VK
from Secret import get
from DateTime import Now, Today, ToDateTime


def run(vk: VK, s3: S3):
    try:
        print("Воркер запустился: " + Now())

        for id in get('ids', ','):
            log_activity(id, vk, s3)

        print("Воркер завершился: " + Now())
    except Exception as ex:
        print("Воркер завершился с ошибкой: " + Now() + '\n' + str(ex))


def log_activity(id: str, vk: VK, s3: S3):
    user_info = vk.get_user_info(id)

    if 'response' in user_info.keys() and type(user_info['response']) == type([]) and len(user_info['response']) > 0:
        first = user_info['response'][0]

        if 'last_seen' in first.keys():
            user_info['last_activity'] = ToDateTime(first['last_seen']['time'], +3)
        if 'online' in first.keys():
            user_info['online'] = str(first['online']) == '1'

        s3.put_async(
            key=f"{Today()}/{id}/{Now()}.json",
            object=user_info
        )