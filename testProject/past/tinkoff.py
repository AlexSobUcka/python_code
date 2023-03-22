def count_slice(m):
    if n == 1:
        return 0
    count = 0
    while m > 1:
        m = m / 2
        count += 1
    return count


n = int(input())
print(count_slice(n))
