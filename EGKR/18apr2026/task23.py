def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    if x == 73:
        return 0
    m = [
        f(x-3, end),
        f(x-8, end),
        f(x//2, end),
    ]
    return sum(m)

res = f(76, 41) * f(41, 12)
print(res)