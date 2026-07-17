def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    if x == 7:
        return 0
    m = [
        f(x+1, end),
        f(x+3, end),
        f(x*2, end),
    ]
    return sum(m)

res = f(2, 15) * f(15, 25)
print(res)

# 2716