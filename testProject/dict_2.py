lst1 = [1, 2, 3,  3, 4, 5]
lst2 = [[1, 2], [3], [4, 5, 6]]
lst3 = [1, [2, 2], [30, [20, 10]]]


def has_duplicates(lst):
    d = set(lst)
    print(d)


print(has_duplicates(lst1))