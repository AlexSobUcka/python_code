class Time:
    """Определяет время суток.
    атрибуты: hour, minute, second
    """


def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


def is_after(t1, t2):
    time1 = t1.hour * 3600 + t1.minute * 60 + t1.second
    time2 = t2.hour * 3600 + t2.minute * 60 + t2.second
    return time1 <= time2


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 40

print_time(time)