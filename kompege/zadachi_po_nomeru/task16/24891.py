from sys import setrecursionlimit
setrecursionlimit(100000)

def f(n):
    if n <= 10:
        return n
    return n - 7 + f(n-21)

res = (f(185734) - f(185650)) // f(40)
print(res)

# 17274