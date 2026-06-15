from pprint import pprint
from math import dist
from collections import Counter

with open('27B_30475.txt') as f:
    m = f.readlines()

m = [x.replace(',', '.').split() for x in m]
m = [[float(a), float(b), c] for a, b, c in m]
m = [[i, x] for i, x in enumerate(m)]
# pprint(m)
ind = [i for i, x in m]
print(Counter(ind))


gap = 1
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1][:2], m[j][1][:2]) <= gap:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

# pprint(m)
m0 = [point for i, point in m if i == 0]
m1 = [point for i, point in m if i == 1]
m3 = [point for i, point in m if i == 3]
print(len(m0), len(m1), len(m3), len(m))
# 2050 2100 2000 6150

# m0 = [x for x in m0 if x[2][-2:] == 'IV']
# m1 = [x for x in m1 if x[2][-2:] == 'IV']
# m3 = [x for x in m3 if x[2][-2:] == 'IV']
# print(len(m0), len(m1), len(m3), len(m))
# 313 303 302 6150

c0 = min(m0, key=lambda a: sum(dist(a[:2], b[:2]) for b in m0))
c3 = min(m3, key=lambda a: sum(dist(a[:2], b[:2]) for b in m3))
b1 = int(dist(c0[:2], c3[:2]) * 10_000)

m0 = [x for x in m0 if x[2][0] == 'A' and x[2].count('I') == 1 and 'V' not in x[2]]
m1 = [x for x in m1 if x[2][0] == 'A' and x[2].count('I') == 1 and 'V' not in x[2]]
m3 = [x for x in m3 if x[2][0] == 'A' and x[2].count('I') == 1 and 'V' not in x[2]]
print(len(m0), len(m1), len(m3), len(m))
# 35 35 43 6150
d0 = max([dist(a[:2], b[:2]) for a in m0 for b in m0])
d1 = max([dist(a[:2], b[:2]) for a in m1 for b in m1])
d3 = max([dist(a[:2], b[:2]) for a in m3 for b in m3])
pprint(d0, d1, d3)
# 5.720611617168377 5.835701093541066 5.768411712873834
b2 = int(max(d0, d1, d3) * 10_000)

print(b1, b2)
