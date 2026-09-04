from math import dist
from collections import Counter

with open('a_27801.txt') as f:
    m = [[float(a) for a in x.replace(',', '.').split()] for x in f.readlines()]

m = [[i, p] for i, p in enumerate(m)]

d = 5
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1], m[j][1]) <= d:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

ind = [i for i, p in m]
print(Counter(ind))

m0 = [p for i, p  in m if i == 0]
m1 = [p for i, p  in m if i == 102]

c0 = min(m0, key=lambda p: sum(dist(p, q) for q in m0))
c1 = min(m1, key=lambda p: sum(dist(p, q) for q in m1))

a1 = len(m0)
a2 = int((dist(c0, [2, 1]) + dist(c1, [2, 1]))*10_000)
print(a1, a2)

# 100 533334
