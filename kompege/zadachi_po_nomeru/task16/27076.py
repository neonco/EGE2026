from functools import cache

@cache
def f(n):
    if n < 43:
        return g(n+4)
    return 2*f(n-2) - f(n-4) + 2

@cache
def g(n):
    if n < 11_240:
        return g(n+3) + 2
    return q(n)

@cache
def q(n):
    if n < 21:
        return n + 4
    return q(n-4) + 2


for i in range(1, 20000):
    q(i)

for i in range(10000, 1, -1):
    g(i)

for i in range(1, 10000):
    f(i)

print(f(2026))