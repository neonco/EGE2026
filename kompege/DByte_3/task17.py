from itertools import pairwise

with open('17_20342.txt') as f:
    m = [int(s) for s in f.readlines()]

max42 = -99999999999
count = 0

t = []
for x in m:
    s = str(abs(x))
    if len(s) == 5 and s[-2:] == '42':
        max42 = max(x, max42)
        t.append((1, x))
    else:
        t.append((0, x))

res = []
for a, b in pairwise(t):
    if a[0] + b[0] == 1:
        if a[1] * a[1] + b[1] * b[1] >= max42 * max42:
            res.append(a[1]+b[1])

print(len(res), max(res))



