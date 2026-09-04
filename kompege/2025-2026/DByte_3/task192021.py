def f(s, target, hod=0):
    flag = target % 2 == hod % 2
    if s >= 100:
        return flag
    if hod > target:
        return False
    m = [
        f(s+2, target, hod+1),
        f(s+4, target, hod+1),
        f(s*2, target, hod+1),
    ]
    return all(m) if flag else any(m)

for s in range(1, 99+1):
    for t in range(9):
        if f(s, t):
            print(s, t)
            break

# 20  24 44
# 21  42
# 19  48