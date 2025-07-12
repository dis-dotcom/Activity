from datetime import datetime, timezone, timedelta


def Now():
    now = datetime.now(timezone.utc) + timedelta(hours=3)
    return now
