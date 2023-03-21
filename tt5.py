def count_normal_segments(changes):
    count_normal = 0
    for i in range(len(changes)):
        sum_i = sum(changes[:i + 1])
        if sum_i == 0:
            count_normal += len(changes) - i
            break
    return count_normal


n = int(input())
lst = list(input().split())
lst = list(map(int, lst))

sum_count = 0
for x in range(len(lst)-1):
    sum_count += count_normal_segments(lst)
    lst.pop(0)

print(sum_count)