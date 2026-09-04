from functools import cache

@cache
def f(x, end):
    if x == end: return 1
    if x > end: return 0
    return f(x+1, end) + f(x+5, end) + f(x*5, end)


res = f(1, 10)*f(10, 30) + f(1, 20)*f(20, 30) - f(1, 10)*f(10, 20)*f(20, 30)*2
print(res)

# 1316