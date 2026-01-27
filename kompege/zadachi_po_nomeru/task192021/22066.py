def f(a, b, t, h=0):
    flag = t % 2 == h % 2
    if a + b >= 100:
        return flag
    if h > t:
        return False
    m = [
        f(a+3, b, t, h+1),
        f(a, b+3, t, h+1),
        f(a*2, b, t, h+1),
        f(a, b*2, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(1, 82+1):
    for t in range(7):
        if f(17, s, t):
            print(s, t)
            break


# 19 - 40
# 20 - 20 29
# 21 - 36