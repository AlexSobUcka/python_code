def profit_list(list_val):
    temp_lst = []
    for value in list_val:
        for i in range(len(value)):
            profit = (9 - int(value[i])) * 10**(len(value)-1 - i)
            temp_lst.append(profit)

    temp_lst.sort(reverse=True)
    return temp_lst


def count_profit(list_val, count):
    sum = 0
    if len(list_val) > count:
        i = 0
        while i < count:
            sum += list_val[i]
            i += 1
    else:
        for i in list_val:
            sum += i

    return sum


n, k = list(map(int, input().split()))
lst = list(input().split())
profit_list = profit_list(lst)
profit = count_profit(profit_list, k)
print(profit)