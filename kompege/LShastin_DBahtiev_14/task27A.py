from pprint import pprint
from math import dist

with open('27A_30475.txt') as f:
    m = f.readlines()

m = [x.replace(',', '.').split() for x in m]
m = [[float(a), float(b), c] for a, b, c in m]
m = [[i, x] for i, x in enumerate(m)]
# pprint(m)

gap = 1
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1][:2], m[j][1][:2]) <= gap:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

# pprint(m)

m0 = [point for i, point in m if i == 0]
m10 = [point for i, point in m if i == 10]
print(len(m0), len(m10))
c0 = min(m0, key=lambda a: sum(dist(a[:2], b[:2]) for b in m0))
m0 = [x for x in m0 if 'O' in x[2] and 'I' not in x[2]]
print(m0)
a = min(m0, key=lambda a: dist(a[:2], c0[:2]))
print(c0)
ax, ay = int(a[0]*10000), int(a[1]*10000)
print(ax, ay)

# 80597 31844

