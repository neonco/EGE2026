def f(s, t, h=0):
    flag = t % 2 == h % 2
    if s >= 124:
        return flag
    if h > t:
        return False
    m = [
        f(s+1, t, h+1),
        f(s+5, t, h+1),
        f(s*3, t, h+1),
    ]
    return all(m) if flag else any(m)


for s in range(1, 123+1):
    for t in range(8):
        if f(s, t):
            print(s, t)
            break

# 19  41
# 20  36 40
# 21  35