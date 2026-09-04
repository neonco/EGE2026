from sys import setrecursionlimit
setrecursionlimit(1000_000)

def f(n):
    if n < 57:
        return 6 * (g(n-7) - 31)
    return 1790 + f(n-5)

def g(n):
    if n < 221440:
        return -3 + g(n+13)
    return 52 + n/60

res = f(1614)
print(res)

# 274193