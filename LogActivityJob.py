from S3 import S3
from VK import VK
from Secret import get
from Logger import Logger
from DateTime import Now, Today, ToDateTime


job_name = 'LogActivityJob'


def run(vk: VK, s3: S3):
    Logger.info(f"Воркер {job_name} запустился: {Now()}")
    try:
        now, today = Now(), Today()

        for x, key in ((x, f"{today}/{x}/{now}.json") for x in get('ids', ',')):
            user_info = vk.get_user_info(x)

            try:
                ticks = user_info['response'][0]['last_seen']['time']
                user_info['last_activity'] = ToDateTime(ticks, +3)
            except Exception as ex:
                Logger.error('Не удалось установить "last_activity"', ex)

            try:
                online = str(user_info['response'][0]['online']) == '1'
                user_info['online'] = online
            except Exception as ex:
                Logger.error('Не удалось установить "online"', ex)

            s3.put_async(key, user_info)

            Logger.info(f'Создан файл {key}')

        Logger.info(f"Воркер {job_name} завершился: {Now()}")
    except Exception as ex:
        Logger.error(f"Воркер {job_name} завершился с ошибкой: {Now()}", ex)
