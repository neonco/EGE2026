from pprint import pprint
from collections import Counter
from math import dist


with open('27_B_29979.txt') as f:
    m = [[float(coord) for coord in s.replace(',', '.').split()] for s in f.readlines()]


gap = 2
m = [[i, p] for i, p in enumerate(m)]
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1], m[j][1]) <= gap:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

# pprint(m)
pprint(Counter([i for i, p in m]))
m0 = [p for i, p in m if i == 0]
m2 = [p for i, p in m if i == 2]
m5 = [p for i, p in m if i == 5]
c0 = min(m0, key=lambda p: sum(dist(p, q) for q in m0))
c2 = min(m2, key=lambda p: sum(dist(p, q) for q in m2))
c5 = min(m5, key=lambda p: sum(dist(p, q) for q in m5))
print(c0, c2, c5)
b1 = len([(x, y) for x, y in m2 if c2[0] - 1 < x < c2[0] + 1 and c2[1] - 1 < y < c2[1] + 1])
b2 = int(abs(c0[1] - c5[1]) * 10_000)
print(b1, b2)

# 132 127070


