from math import dist
from collections import Counter

with open('27B_18678.txt') as f:
    m = [[float(x) for x in s.replace(',','.').split()] for s in f.readlines()]

print(len(m))

cl = list(range(len(m)))

for i, p in enumerate(m):
    if i % 100 == 0:
        print(i)
    for j, q in enumerate(m):
        if dist(p, q) <= 1:
            cl[i] = min(cl[i], cl[j])
            cl[j] = cl[i]

print(cl)
print(Counter(cl))
# Counter({2: 3331, 1: 3329, 0: 3327, 941: 5, 1710: 4, 1912: 3})
m1 = [p for i, p in enumerate(m) if cl[i] == 0]
m2 = [p for i, p in enumerate(m) if cl[i] == 1]
m3 = [p for i, p in enumerate(m) if cl[i] == 2]

def center(cluster):
   return min(cluster, key=lambda p: sum(dist(p, q) for q in cluster))

c1 = center(m1)
c2 = center(m2)
c3 = center(m3)

px = (c1[0] + c2[0] + c3[0]) / 3
py = (c1[1] + c2[1] + c3[1]) / 3

print(int(px*100000), int(py*100000))

# 455364 406022

