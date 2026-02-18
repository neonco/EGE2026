from math import dist

with open('27_A_25364.txt') as f:
    m = [[float(x) for x in s.replace(',','.').split()] for s in f.readlines()]

print(m)

m1 = [[x, y] for x, y in m if y > 10]
m2 = [[x, y] for x, y in m if y < 10]

print(len(m1), len(m2), len(m))

def sum_dist(point, clust):
    res = 0
    for p in clust:
        res += dist(point, p)
    return res

m1 = [[sum_dist((x, y), m1), x, y] for x, y in m1]
m2 = [[sum_dist((x, y), m2), x, y] for x, y in m2]


cl1 = min(m1)[1:]
cl2 = min(m2)[1:]

print(cl1, cl2)

res1 = int(dist((1, 1), cl1) * 10000)
res2 = int(dist((1, 1), cl2) * 10000)

print(min(res1, res2), max(res1, res2))