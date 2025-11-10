from functools import cache

@cache
def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    if x == 8:
        return 0
    return f(x-2, end) + f(x-5, end) + f(x//4, end)


res = f(23, 15), f(15, 3)
print(res)