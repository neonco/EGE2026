def f(x, end, d=2, tr=''):
    if x == end:
        p.add(tr)
        return 1
    if x > end:
        return 0
    if x == 33:
        return 0
    return f(x+1, end, 2, tr+f'{x}') + f(x+d, end, d+1, tr+f'{x}')


p = set()
f(2, 21)
a = len(set(p))
p = set()
f(21, 45)
b = len(set(p))

print(a, b, a*b)
# 3147 7914 24905358 ответ ниочень