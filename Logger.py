class Logger:
    logs = []

    @staticmethod
    def info(message: str):
        Logger.log('INFO', message)

    @staticmethod
    def error(message: str, ex: Exception=None):
        ex_str = '' if ex is None else '\n' + str(ex)
        Logger.log('ERROR', f'{message}{ex_str}')

    @staticmethod
    def log(level: str, message: str):
        if len(Logger.logs) > 10000:
            Logger.logs = Logger.logs[100:]

        Logger.logs.append((level, message))
