from math import dist
from collections import Counter

with open('27_A_28766.txt') as f:
    m = [s.replace(',', '.').split() for s in f.readlines()]

m = [[float(x), float(y), cat[0], int(cat[1]), cat[2:]] for x, y, cat in m]
print(m[0])
mi = [[i, *x] for i, x in enumerate(m)]
print(mi[0])
for i in range(len(mi)):
    for j in range(len(mi)):
        p, q = mi[i][1:3], mi[j][1:3]
        if dist(p, q) <= 1:
            mi[i][0] = mi[j][0] = min(mi[i][0], mi[j][0])
ind = [x[0] for x in mi]
print(Counter(ind))

m4 = [x[1:3] for x in mi if x[0] == 4]
centr4 = min(m4, key=lambda p: sum(dist(p, q) for q in m4))
print(centr4)
m_red_giant = [x[1:3] for x in mi if x[3] == 'Y' and x[5] == 'III']
print(m_red_giant)
a1 = min(m_red_giant, key=lambda p: dist(p, centr4))
a2 = max(m_red_giant, key=lambda p: dist(p, centr4))
a1 = int(dist(centr4, a1) * 10_000)
a2 = int(dist(centr4, a2) * 10_000)
print(a1, a2)