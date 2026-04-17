def f(s, target, hod=0):
    flag = (target % 2 == hod % 2)
    if s > 272:
        return flag
    if hod > target:
        return False
    m = [
        f(s+2, target, hod+1),
        f(s+5, target, hod+1),
        f(s*4, target, hod+1),
    ]
    # return all(m) if flag else any(m)
    if flag:
        return any(m)
    else:
        return any(m)

for s in range(1, 272+1):
    for t in range(7):
        if f(s, t):
            print(s, t)
            break

# 19 18
# 20 17 62
# 21 60



