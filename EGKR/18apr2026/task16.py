import sys
sys.setrecursionlimit(1_000_000)

def f(n):
    if n >= 21:
        return f(n-8) + 1095
    return 10 * (g(n-7) - 36)

def g(n):
    if n >= 22_560:
        return n // 23 + 33
    return g(n + 11) - 4

res = f(548)
print(res)