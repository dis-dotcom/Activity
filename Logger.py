class Logger:
    logs = []

    @staticmethod
    def info(message: str):
        Logger.log(f'INFO:\t{message}')

    @staticmethod
    def error(message: str, ex: Exception=None):
        ex_str = '' if ex is None else '\n' + str(ex)
        Logger.log(f'ERROR:\t{message}{ex_str}')

    @staticmethod
    def log(message: str):
        if len(Logger.logs) > 10000:
            Logger.logs = Logger.logs[100:]

        Logger.logs.append(message)
