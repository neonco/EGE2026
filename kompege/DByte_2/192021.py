def f(s, t, h=0):
    flag = h%2 == t%2
    if s <= 20:
        return flag
    if h > t:
        return False
    m = [
        f(s-5, t, h+1),
        f(s-7, t, h+1),
        f(s//4, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(21, 1400):
    for t in range(1, 7):
        if f(s, t):
            print(s, t)
            break
# 84 2
# 89 3
# 90 3
# 96 4