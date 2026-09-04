def f(s, t, h=0):
    flag = (t%2 == h%2)
    if s <= 40:
        return flag
    if h > t:
        return False
    m = [
        f(s-4, t, h+1),
        f(s-6, t, h+1),
        f(s//3, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(41, 30000):
    for t in range(7):
        if f(s, t):
            print(s, t)
            break

# 249
# 379 380
# 8
