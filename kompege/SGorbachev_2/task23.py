def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    if x == 15:
        return 0
    return f(x+2, end) + f(x+5, end) + f(x*3, end)


res = f(1, 10) * f(10, 31)
print(res)