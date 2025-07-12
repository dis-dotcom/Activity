from datetime import datetime, timedelta


def Now():
    now = datetime.now() + timedelta(hours=3)
    return now
