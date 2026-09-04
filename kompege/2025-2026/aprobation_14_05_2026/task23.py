def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    if x == 9:
        return 0
    return f(x-1, end) + f(x-3, end) + f(x//2, end)

res = f(19, 12) * f(12, 3)

print(res)

# 153

