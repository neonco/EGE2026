def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    if x == 26:
        return 0
    return f(x-4, end) + f(x-7, end) + f(x//3, end)


print(f(91, 41) * f(41, 14))

# 249