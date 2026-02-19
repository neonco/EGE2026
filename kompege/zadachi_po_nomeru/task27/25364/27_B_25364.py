from math import dist

with open('27_B_25364.txt') as f:
    m = [[float(x) for x in s.replace(',','.').split()] for s in f.readlines()]

print(len(m))

m1 = [[x, y] for x, y in m if y > 22]
m2 = [[x, y] for x, y in m if 15 < y < 22]
m3 = [[x, y] for x, y in m if y < 15]

def center(cluster):
   return min(cluster, key=lambda p: sum(dist(p, q) for q in cluster))

c1 = center(m1)
c2 = center(m2)
c3 = center(m3)

print(c1, c2, c3)
print(len(m1), len(m2), len(m3))
# самый большой кластер m3

q1 = len([p for p in m3 if dist(p, c3) <= 1.2])
q2 = len([p for p in m3 if dist(p, c3) <= 0.75])
print(q1, q2)

# 358 203
