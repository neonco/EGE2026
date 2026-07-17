from math import dist

with open('27_A_25300.txt') as file:
    m = file.readlines()

m = m[1:]
m = [s.replace(',', '.') for s in m]
m = [s.split() for s in m]
m = [[float(x), float(y)] for x, y in m]

m1 = [[x, y] for x, y in m if 0 <= x <= 10]
m2 = [[x, y] for x, y in m if 11 <= x <= 21]
m3 = [[x, y] for x, y in m if 22 <= x <= 30]
# print(len(m), len(m1) + len(m2) + len(m3))
# выкинуты 3 аномальные точки

def perebor_cluster(cluster):
    res = []
    for center in cluster:
        sdist = 0
        for point in cluster:
            sdist += dist(center, point)
        res.append([sdist, center])
    return min(res)[1]

c1 = perebor_cluster(m1)
c2 = perebor_cluster(m2)
c3 = perebor_cluster(m3)
print(c1, c2, c3)

res = []
for center in [c1, c2, c3]:
    for point in m:
        res.append([dist(center, point), center])

p1 = sum(max(res)[1])
p2 = max(res)[0]
print(p1, p2)

# 28  42