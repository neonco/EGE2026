def f(a, b, target, h=0):
    flag = target % 2 == h % 2
    if a + b <= 200:
        return flag
    if h > target:
        return False
    m = [
        f(a-3, b-4, target, h+1),
        f(a-8, b//2, target, h+1),
        f(a//2, b-10, target, h+1),
    ]
    return all(m) if flag else any(m)


for b in range(100, 300):
    for t in range(7):
        if f(110, b, t):
            print(b, t)
            break
