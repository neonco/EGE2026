def f(a, b, t, h=0):
    flag = h%2 == t%2
    if a + b >= 65:
        return flag
    if h > t:
        return False
    m = [
        f(a+1, b, t, h+1),
        f(a, b+1, t, h+1),
        f(a*3, b, t, h+1),
        f(a, b*3, t, h+1),
    ]
    return all(m) if flag else any(m)


for s in range(1, 58+1):
    for t in range(8):
        if f(6, s, t):
            print(s, t)
            break

# 19 7
# 21 10 19
# 22 18