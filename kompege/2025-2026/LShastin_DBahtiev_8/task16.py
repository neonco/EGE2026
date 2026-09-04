from functools import cache

@cache
def f(n):
    if n < 20:
        return 10
    if n % 2 == 0:
        return f(n//2) + n - 3
    return f(n-2) + 6

for n in range(10, 1_000_000):
    if f(n) >= 1_000_000:
        print(n, f(n))
        break

# 333349
