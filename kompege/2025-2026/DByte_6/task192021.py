def f(s, t, h=0):
    flag = t % 2 == h % 2
    if s >= 77:
        return flag
    if h > t:
        return False
    m = [
        f(s+1, t, h+1),
        f(s+4, t, h+1),
        f(s*2, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(1, 77):
    for t in range(7):
        if f(s, t):
            print(s, t)
            break