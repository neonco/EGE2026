def f(s, t, h=0):
    flag = t % 2 == h % 2
    if s <= 20:
        return flag
    if h > t:
        return False
    m = [
        f(s-2, t, h+1),
        f(s-4, t, h+1),
        f(s//2, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(21, 600):
    for t in range(7):
        if f(s, t):
            print(s, t)
            break

# 20   44 45
# 21   48
# 19   42