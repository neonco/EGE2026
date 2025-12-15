def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    if x == 36:
        return 0
    m = [
        f(x-3, end),
        f(x-6, end),
        f(x//2, end),
    ]
    return sum(m)

res = f(86, 53) * f(53, 12)
print(res)

# 144