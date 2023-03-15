def max_list(list_val, count, total):
    if count >= total:
        return list_val
    else:
        list_val.sort(reverse=True)
        temp_lst = []
        for i in list_val:
            if len(i) >= len(list_val[count-1]):
                print(i)
            else:
                pass


n, k = list(map(int, input().split()))
lst = list(input().split())
print(max_list(lst, k, n))

