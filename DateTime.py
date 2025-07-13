from datetime import datetime, timezone, timedelta


def Now() -> str:
    now = datetime.now(timezone.utc) + timedelta(hours=3)
    return formatDateTime(now)


def Today() -> str:
    now = datetime.now(timezone.utc) + timedelta(hours=3)
    return formatDate(now)


def ToDateTime(ticks, utc=0):
    return formatDateTime(datetime.fromtimestamp(ticks) + timedelta(hours=utc))


def formatDateTime(x):
    milliseconds = x.microsecond // 1000
    return x.strftime("%Y-%m-%d %H:%M:%S") + f".{milliseconds:03d}"


def formatDate(x):
    return x.strftime("%Y-%m-%d")
