import time

print (time.time())
def time_to_human(time):
    days = time // (60 * 60 * 24)
    hours = int(time // (60 * 60) % 24)
    minutes = int(time // 60 % 60)
    seconds = int(time % 60 // 1)
    if seconds < 10:
        print('%s days and %s:%s:0%s' % (days, hours, minutes, seconds))
    else:
        print('%s days and %s:%s:%s' % (days, hours, minutes, seconds))

time_to_human(time.time())
