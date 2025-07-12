import os


def get(arg_name):
    arg = os.getenv(arg_name)

    if arg is None or '':
        raise Exception('Отсутствует параметр ' + arg_name)

    return arg
