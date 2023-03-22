def if_down(lst):
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            pass
        else:
            return False
    return True


def if_up(lst):
    for i in range(len(lst)-1):
        if lst[i] <= lst[i+1]:
            pass
        else:
            return False
    return True

def in_order(lst):
    if if_down(lst) or if_up(lst):
        print('YES')
    else:
        print('NO')


lst = list(input().split())
in_order(lst)