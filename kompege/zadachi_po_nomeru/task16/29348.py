from functools import cache

@cache
def f(n):
    if n < 10:
        return 1
    return (n+3) * f(n-3)

for n in range(1, 2500_000):
    f(n)

res = (f(2470_563) // 519 - 477*f(2470_560)) // f(2470_557)
print(res)