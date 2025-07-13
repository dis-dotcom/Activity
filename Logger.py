class Logger:
    @staticmethod
    def info(message: str):
        print(f'INFO:\t{message}')

    @staticmethod
    def error(message: str, ex: Exception=None):
        ex_str = '' if ex is None else '\n' + str(ex)
        print(f'ERROR:\t{message}{ex_str}')
