from datetime import datetime, timezone, timedelta


def Now() -> str:
    utc = datetime.now(timezone.utc)
    local = utc + timedelta(hours=3)

    return formatDateTime(local)


def Today() -> str:
    utc = datetime.now(timezone.utc)
    local = utc + timedelta(hours=3)

    return formatDate(local)


def ToDateTime(ticks, hours=0):
    utc = datetime.fromtimestamp(ticks, tz=timezone.utc)
    local = utc + timedelta(hours=hours)

    return formatDateTime(local)


def formatDateTime(x):
    milliseconds = x.microsecond // 1000
    return x.strftime("%Y-%m-%d %H:%M:%S") + f".{milliseconds:03d}"


def formatDate(x):
    return x.strftime("%Y-%m-%d")
