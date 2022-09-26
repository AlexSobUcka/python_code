def nested_sum(t):
    total = 0
    for i in t:
        if type(i) is list:
            total += nested_sum(i)
        else:
            total += i
    return total


def scum(t):
    cum_list = [t[0]]
    for i in range(1, len(t)):
        cum_list += [cum_list[i-1] + t[i]]
    return(cum_list)


def middle(t):
    midst = t[1:-1]
    return midst


def chop(t):
    del t[0], t[-1]


def is_sorted(t):
    if t == sorted(t):
        return True
    else:
        return False


lst1 = [1, 2, 2, 3, 4, 5]
lst2 = [[1, 2], [3], [4, 5, 6]]
lst3 = [1, [2, 2], [30, [20, 10]]]

print(sorted(lst1))

print(middle(lst1))
print(is_sorted(lst1))
chop(lst1)
print(scum(lst1))
print(middle(lst1))
print(nested_sum(lst2))
print(nested_sum(lst3))
