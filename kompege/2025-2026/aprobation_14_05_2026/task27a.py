from pprint import pprint
from collections import Counter
from math import dist


with open('27_A_29979.txt') as f:
    m = [[float(coord) for coord in s.replace(',', '.').split()] for s in f.readlines()]


gap = 4
m = [[i, p] for i, p in enumerate(m)]
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1], m[j][1]) <= gap:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

# pprint(m)
pprint(Counter([i for i, p in m]))
m0 = [p for i, p in m if i == 0]
m3 = [p for i, p in m if i == 3]
c0 = min(m0, key=lambda p: sum(dist(p, q) for q in m0))
c3 = min(m3, key=lambda p: sum(dist(p, q) for q in m3))
a1 = len([p for p in m0 if p[0] <= c0[0]])
a2 = int(dist(c0, c3)*10_000)
print(a1, a2)


