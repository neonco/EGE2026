from functools import cache

@cache
def f(n):
    if n >= 20:
        return f(n-5) + 3219
    return 8 * g((n-9) - 34)

@cache
def g(n):
    if n >= 250_000:
        return n // 24 + 32
    return g(n+9) - 3

for i in range(250_000, 1, -1):
    g(i)

for i in range(1, 250_000):
    f(i)

print(f(925))
# 2698