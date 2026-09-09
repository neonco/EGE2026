from sys import setrecursionlimit

setrecursionlimit(5000)

def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)

res = (f(3038) + 5 * f(3037)) / f(3036)
print(res)

# 9241591