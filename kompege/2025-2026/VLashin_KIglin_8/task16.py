from sys import setrecursionlimit

setrecursionlimit(200_000)

def f(n):
    if n >= 4300:
        return g(n-3)
    return f(n+2) + 2


def g(n):
    if n >= 11:
        return g(n-3) + 5
    return q(n) + 6


def q(n):
    if n >= 210_000:
        return n + 4
    return q(n+3) + 2

print(f(1))

# 361458