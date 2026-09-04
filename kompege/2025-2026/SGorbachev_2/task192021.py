def f(s, t, h=0):
    flag = t % 2 == h % 2
    if s <= 14:
        return flag
    if h > t:
        return False
    m = [
        f(s-4, t, h+1),
        f(s-7, t, h+1),
        f(s//2, t, h+1),
    ]
    return all(m) if flag else any(m)

for s in range(15, 100):
    for t in range(0, 7):
        if f(s, t):
            print(s, t)
            break


#34 35