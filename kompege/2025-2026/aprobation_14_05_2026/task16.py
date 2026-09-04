from sys import setrecursionlimit
setrecursionlimit(30000)

def f(n):
    return 3*g(n-3) + 7

def g(n):
    if n <= 20:
        return n + 2
    return g(n-3) + 1

res = f(37811)
print(res)

# 37861