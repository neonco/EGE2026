from math import dist
from collections import Counter

with open('27_B_27637.txt') as f:
    m = [s.replace(',','.').split() for s in f.readlines()]

m = [[float(x), float(y)] for x, y in m]
m = [[i, point] for i, point in enumerate(m)]


for i in range(len(m)):
    for j in range(i+1, len(m)):
        if dist(m[i][1], m[j][1]) <= 2:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

# for x in m:
#     print(*x)
cl = [i for i, point in m]
print(Counter(cl))
print(len(m))

m1 = [p for i, p in m if i == 0]   # 902
m2 = [p for i, p in m if i == 2]   # 200
m3 = [p for i, p in m if i == 5]   # 148

m1 = [(sum([dist(c, p) for p in m1]), c) for c in m1]
m2 = [(sum([dist(c, p) for p in m2]), c) for c in m2]
m3 = [(sum([dist(c, p) for p in m3]), c) for c in m3]


c2 = min(m2)[1]
b1 = len([x for x in m2 if dist(x[1], c2) <= 1.6 and x[1] != c2])
print(b1)

c1 = min(m1)[1]
b2 = [x for x in m1 if dist(x[1], c1) > 2.67][0][1]
b2 = dist(b2, c1) * 10_000

print(int(b2))

