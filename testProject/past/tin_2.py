def count_slice(n):
    i = 0
    m = n
    while m > 1:
        m = m//2
        i += 1
    print(i)
    if n > i*2:
        i += 1
    return i


n = int(input())
print(count_slice(n))