def f(a, b, c, t, h=0):
    flag = t % 2 == h % 2
    if a + b + c >= 73:
        return flag
    if h > t:
        return False
    m = [
        f(a+3, b, c, t, h+1),
        f(a, b+3, c, t, h+1),
        f(a, b, c+3, t, h+1),
        f(a+13, b, c, t, h+1),
        f(a, b+13, c, t, h+1),
        f(a, b, c+13, t, h+1),
        f(a+23, b, c, t, h+1),
        f(a, b+23, c, t, h+1),
        f(a, b, c+23, t, h+1),
    ]
    return any(m) if flag else any(m)

for s in range(1, 23+1):
    for t in range(7):
        if f(2, s, 2*s, t):
            print(s, t)
            break


# 19 - 9
# 20 - 11 14
# 21 - 10 13