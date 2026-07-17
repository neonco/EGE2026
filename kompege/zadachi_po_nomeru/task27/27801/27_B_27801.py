from math import dist
from collections import Counter

with open('b_27801.txt') as f:
    m = [[float(a) for a in x.replace(',', '.').split()] for x in f.readlines()]

m = [[i, p] for i, p in enumerate(m)]

d = 7
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1], m[j][1]) <= d:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

ind = [i for i, p in m]
print(Counter(ind))

m0 = [p for i, p  in m if i == 453]
m1 = [p for i, p  in m if i == 203]
m2 = [p for i, p  in m if i == 0]

c0 = min(m0, key=lambda p: sum(dist(p, q) for q in m0))
c1 = min(m1, key=lambda p: sum(dist(p, q) for q in m1))
c2 = min(m2, key=lambda p: sum(dist(p, q) for q in m2))

print(c0, c1, c2)
b1 = len([p for p in m1 if dist(p, c1) <= 2])
b2 = max(dist(c0, p) for p in m0)
b2 = int(b2 * 10000)

print(b1, b2)

