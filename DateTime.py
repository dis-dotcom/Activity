from datetime import datetime, timezone, timedelta


def Now():
    now = datetime.now(timezone.utc) + timedelta(hours=3)
    return formatDateTime(now)


def Today():
    now = datetime.now(timezone.utc) + timedelta(hours=3)
    return formatDate(now)


def ToDateTime(ticks):
    return formatDateTime(datetime.fromtimestamp(ticks))


def formatDateTime(x):
    milliseconds = x.microsecond // 1000
    return x.strftime("%Y-%m-%d %H:%M:%S") + f".{milliseconds:03d}"


def formatDate(x):
    return x.strftime("%Y-%m-%d")
