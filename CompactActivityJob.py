from S3 import S3
from DateTime import Now

def run(s3: S3):
    try:
        now = Now()
        print(f"Воркер запустился: {now}")
        run_internal(s3)
        print(f"Воркер завершился: " + Now())
    except Exception as ex:
        print(f"Воркер завершился с ошибкой: {Now()}" + '\n' + str(ex))


def run_internal(s3: S3):
    objects = [get_file_info(obj) for obj in s3.get_objects('')]

    for _, groups_id in group_by(lambda x: x['id'], objects):
        for _, groups_date in group_by(lambda x: x['date'], groups_id):
            if len(groups_date) > 1: merge(groups_date)


def merge(files):
    for file in files:
        print(file['full_path'])


def group_by(selector, items) -> dict:
    groups = {}
    for key, value in [(selector(item), item) for item in items]:
        if key not in groups.keys():
            groups[key] = []
        groups[key].append(value)

    return groups


def get_file_info(x: str):
    result = x.split(sep='/')

    return {
        'full_path': x,
        'date': result[0],
        'id': result[1],
        'file_name': result[2]
    }

