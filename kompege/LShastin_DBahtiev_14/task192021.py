def f(a, b, t, h=0):
    flag = t % 2 == h % 2
    if a + b >= 808:
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


for s in range(1, 771+1):
    for t in range(7):
        if f(36, s, t):
            print(t, s)
            break

# 19 193
# 20 367 384
# 21 364