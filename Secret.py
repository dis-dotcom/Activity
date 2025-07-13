import os

isLocal = False

secrets = {

}

def get(arg_name, sep=None):
    arg = secrets[arg_name] if isLocal else os.getenv(arg_name)

    if arg is None or '':
        raise Exception('Отсутствует параметр ' + arg_name)

    if sep:
        arg = arg.split(sep)

    return arg
