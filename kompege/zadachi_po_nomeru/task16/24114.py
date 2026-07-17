from functools import cache

@cache
def f(n):
    return g(n+1)

@cache
def g(n):
    if n >= 30_000:
        return 3
    return g(n+3) + 7

for n in range(30_000, 1000, -100):
    f(n)
    g(n)
res = f(1500)
print(res)