def f(a, b, c, t, h=0):
    flag = h % 2 == t % 2
    if a + b + c >= 94:
        return flag
    if h > t:
        return False
    m = [
        f(a+5, b, c, t, h+1),
        f(a, b+5, c, t, h+1),
        f(a, b, c+5, t, h+1),
        f(a, b*2, c, t, h+1),
        f(a, b, c*3, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(1, 45):
    for t in range(7):
        if f(s, 6, s+5, t):
            print(s, t)
            break

# 19  5
# 20  4 16
# 21  12 + 13 + 15 = 40