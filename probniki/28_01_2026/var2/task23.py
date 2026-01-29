def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    return f(x + 1, end) + f(x + 5, end)


print(f(2, 15))

# 20