from S3 import S3
from VK import VK
from Secret import get
from DateTime import Now, Today, ToDateTime


def run(vk: VK, s3: S3):
    try:
        print("Воркер запустился: " + Now())
        [log_activity(x, vk, s3) for x in get('ids', ',')]
        print("Воркер завершился: " + Now())
    except Exception as ex:
        print("Воркер завершился с ошибкой: " + Now() + '\n' + str(ex))


def log_activity(x: str, vk: VK, s3: S3):
    user_info = vk.get_user_info(x)

    if 'response' not in user_info.keys(): return
    if type(user_info['response']) != type([]): return
    if len(user_info['response']) == 0: return

    if 'last_seen' in user_info['response'][0].keys():
        user_info['last_activity'] = ToDateTime(user_info['response'][0]['last_seen']['time'], +3)

    if 'online' in user_info['response'][0].keys():
        user_info['online'] = str(user_info['response'][0]['online']) == '1'

    s3.put_async(
        key=f"{Today()}/{x}/{Now()}.json",
        object=user_info
    )