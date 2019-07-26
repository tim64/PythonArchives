import time
import datetime
import winsound

dt_utc = datetime.datetime.utcnow()
start = time.mktime(dt_utc.timetuple())
while(1):
    dt_utc = datetime.datetime.utcnow()
    current = time.mktime(dt_utc.timetuple())
    if current == start + 1800:
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        pause = current
        while(1):
            dt_utc = datetime.datetime.utcnow()
            current = time.mktime(dt_utc.timetuple())
            if current == pause + 300:
                winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                break
        start = current

