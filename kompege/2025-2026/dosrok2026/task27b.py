from math import dist
from collections import Counter

with open('27_B_28766.txt') as f:
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

m0 = [x[1:3] for x in mi if x[0] == 0] # 451
m2 = [x[1:3] for x in mi if x[0] == 2] # 100
m5 = [x[1:3] for x in mi if x[0] == 5] # 74
centr0 = min(m0, key=lambda p: sum(dist(p, q) for q in m0))
centr2 = min(m2, key=lambda p: sum(dist(p, q) for q in m2))
centr5 = min(m5, key=lambda p: sum(dist(p, q) for q in m5))
print(centr0, centr2, centr5)
m_yellow_supergiant = [x[0:3] for x in mi if x[3] == 'Z' and x[5] == 'I']
print(m_yellow_supergiant)
b1 = 100000
for i,*p in m_yellow_supergiant:
    for j, *q in m_yellow_supergiant:
        if dist(p, q) > 0 and i == j:
            b1 = min(dist(p, q), b1)
print(b1)
ind_y_s = [x[0] for x in m_yellow_supergiant]
print(Counter(ind_y_s)) # 0: 9, 5: 3, 2: 1
b2 = dist(centr0, centr2)
b1 = int(b1 * 10_000)
b2 = int(b2 * 10_000)
print(b1, b2)
# 1035 125591