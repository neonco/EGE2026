def f(s, t, h=0):
    flag = h % 2 == t % 2
    if s <= 15:
        return flag
    if h > t:
        return False
    m = [
        f(s-3, t, h+1),
        f(s-7, t, h+1),
        f(s//4, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(16, 1000):
    for t in range(7):
        if f(s, t):
            print(s, t)
            break

# 19 64
# 20 67 68
# 21 70