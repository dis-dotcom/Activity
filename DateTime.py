from datetime import datetime, timezone, timedelta


def Now():
    now = datetime.now(timezone.utc) + timedelta(hours=3)
    milliseconds = now.microsecond // 1000
    now_format = now.strftime("%Y-%m-%d %H:%M:%S") + f".{milliseconds:03d}"

    return now_format


def Today():
    now = datetime.now(timezone.utc) + timedelta(hours=3)
    now_format = now.strftime("%Y-%m-%d")

    return now_format

