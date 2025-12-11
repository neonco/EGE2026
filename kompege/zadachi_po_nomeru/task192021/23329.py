from math import ceil
from functools import cache


@cache
def f(a, b, t, h=0):
    flag = t % 2 == h % 2
    if a + b <= 60:
        return flag
    if h > t:
        return False
    m = [
        f(a-5, b, t, h+1),
        f(a, b-3, t, h+1),
        f(a//2, b, t, h+1),
        f(a, ceil(b/2), t, h+1),
    ]
    return all(m) if flag else any(m)

for b in range(5, 150+1):
    for t in range(20):
        if f(130, b, t):
            print(b, t)
            break

# 20   29 30
# 21   34*35*36*61*62 = 162020880
# 19   28   (тут надо было поменять all на any)
