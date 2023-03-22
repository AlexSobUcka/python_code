def count_money(month_price, month_mb, mb_price, mb):
    sum = month_price
    if mb > month_mb:
        sum += (mb - month_mb) * mb_price
    return sum


a, b, c, d = list(map(int, input().split()))
print(count_money(a, b, c, d))
