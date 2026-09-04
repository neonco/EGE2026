from math import dist
from collections import Counter

with open('27_A_27637.txt') as f:
    m = [s.replace(',','.').split() for s in f.readlines()]

m = [[float(x), float(y)] for x, y in m]
m = [[i, point] for i, point in enumerate(m)]


for i in range(len(m)):
    for j in range(i+1, len(m)):
        if dist(m[i][1], m[j][1]) <= 1:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

# for x in m:
#     print(*x)
cl = [i for i, point in m]
print(Counter(cl))
print(len(m))

m1 = [p for i, p in m if i == 0]   # 301
m2 = [p for i, p in m if i == 3]   # 344

m1 = [(sum([dist(c, p) for p in m1]), c) for c in m1]
m2 = [(sum([dist(c, p) for p in m2]), c) for c in m2]

c1 = min(m1)[1]
c2 = min(m2)[1]
p = [-1.0, 1.3]
a2 = (dist(c1, p) + dist(c2, p)) * 10_000
print(int(a2))

