from functools import cache

@cache
def f(a, b, winner, hod=0):
    flag = (winner % 2 == hod % 2)
    if a + b <= 114:
        return flag
    if hod > winner:
        return False
    m = [
        f(a-3, b, winner, hod+1),
        f(a, b-3, winner, hod+1),
        f(a//2, b, winner, hod+1),
        f(a, b//2, winner, hod+1),
    ]
    return any(m) if flag else any(m)

for s in range(55, 4000):
    for w in range(8):
        if f(60, s, w):
            print(s, w)
            break

# 19 - 219
# 20 - 113 225
# 21 - 175