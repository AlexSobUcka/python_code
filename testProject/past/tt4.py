def boring_prefix(value_lst):
    counts = {}
    max_num = 0
    min_num = 1
    boring_index = 0
    temp = []
    for i in range(len(value_lst)):
        if value_lst[i] in counts:
            counts[value_lst[i]] += 1
        else:
            counts[value_lst[i]] = 1
        max_num = max(counts.values())
        min_num = min(counts.values())
        max_count = sum(value == max_num for value in counts.values())
        min_count = sum(value == min_num for value in counts.values())
        if (max_count + min_count == len(counts)) and (max_count == 1 or min_count == 1):
            temp.append(i+1)
        elif max_count == min_count == len(counts):
            temp.append(i + 1)
    temp.sort()
    return temp[-1]

n = int(input())
lst = list(input().split())
print(boring_prefix(lst))