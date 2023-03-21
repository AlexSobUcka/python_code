def check_time(n, m, k):
    total_checks = n * k
    parallel_checks = m
    if parallel_checks <= k:
        return max(n, m)
    else:
        if total_checks % parallel_checks == 0:
            return total_checks // parallel_checks
        return (total_checks // parallel_checks) + 1


n, m, k = list(map(int, input().split()))
print(check_time(n, m, k))