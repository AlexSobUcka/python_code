def shortest_good_substring(s):
    a, b, c, d = -1, -1, -1, -1
    ans = len(s) + 1
    temp = []
    for i in range(len(s)):
        if s[i] == 'a':
            a = i
        elif s[i] == 'b':
            b = i
        elif s[i] == 'c':
            c = i
        elif s[i] == 'd':
            d = i
        #print(a, b, c, d)
        if a != -1 and b != -1 and c != -1 and d != -1:
            ans = min(ans, max(a, b, c, d) - min(a, b, c, d) + 1)
            temp.append(ans)
    temp.sort()
    return temp[0] if ans <= len(s) else -1


n = int(input())
s = input()
print(shortest_good_substring(s))