def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    if x == 22:
        return 0
    return f(x-2, end) + f(x-5, end) + f(x//2, end)


res = f(47, 11)
print(res)