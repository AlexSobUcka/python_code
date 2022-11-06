from random import randint


def random_date():
    date_lst = []
    for i in range(23):
        day = randint(1, 30)
        month = randint(1, 12)
        date = [month, day]
        date_lst.append(date)
    return date_lst

def is_double(t):
    last = []
    for i in sorted(t):
        if i == last:
            return True
        else:
            last = i
    return False


total = 0
success = 0
for i in range(10000):
    if is_double(random_date()):
        success += 1
    total += 1
print(success/total)