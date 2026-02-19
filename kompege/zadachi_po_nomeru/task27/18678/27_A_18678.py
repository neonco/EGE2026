from math import dist
from collections import Counter

with open('27A_18678.txt') as f:
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
# Counter({2: 247, 0: 244, 90: 5, 169: 4})
m1 = [p for i, p in enumerate(m) if cl[i] == 0]
m2 = [p for i, p in enumerate(m) if cl[i] == 2]

def center(cluster):
   return min(cluster, key=lambda p: sum(dist(p, q) for q in cluster))

c1 = center(m1)
c2 = center(m2)

px = (c1[0] + c2[0]) / 2
py = (c1[1] + c2[1]) / 2

print(int(px*100000), int(py*100000))

# 346070 215898