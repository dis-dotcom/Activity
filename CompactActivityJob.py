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

    for groups_id in group_by(lambda x: x['id'], objects).values():
        for groups_date in group_by(lambda x: x['date'], groups_id).values():
            if len(groups_date) > 1: merge(s3, groups_date)


def merge(s3: S3, files: list):
    objects = []

    if len(files) > 60:
        files = files[:60]

    for file in files:
        obj = s3.get_object(file['full_path'])
        if type(obj) == type([]):
            [objects.append(x) for x in obj]
        else:
            obj['created_at'] = str(file['file_name']).rstrip('.json')
        objects.append(obj)

    key, keys = get_keys(list(map(lambda x: x['full_path'], files)))

    s3.put(key, objects)
    [s3.delete_by_key(key) for key in keys]


def group_by(selector, items) -> dict:
    groups = {}
    for key, value in ((selector(item), item) for item in items):
        if key not in groups.keys():
            groups[key] = []
        groups[key].append(value)

    return groups


def get_keys(keys: list) -> (str, list):
    keys = list(sorted(set(keys)))
    key = keys[0]
    keys.remove(key)

    return key, keys

def get_file_info(x: dict):
    result = x['Key'].split(sep='/')

    return {
        'full_path': x['Key'],
        'date': result[0],
        'id': result[1],
        'file_name': result[2]
    }

