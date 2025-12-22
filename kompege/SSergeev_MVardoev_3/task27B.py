from math import dist

with open('27_A_25300.txt') as file:
    m = file.readlines()

m = m[1:]
m = [s.replace(',', '.') for s in m]
m = [s.split() for s in m]
m = [[float(x), float(y)] for x, y in m]

anomaly = [[x, y] for x, y in m if x < 0 or x > 30]
m = [[x, y] for x, y in m if [x, y] not in anomaly]

# print(len(m), len(anomaly))
# вычленены 3 аномальные точки
a, b, c = anomaly
c = [(a[0]+b[0]+c[0])/3, (a[1]+b[1]+c[1])/3]

res = []

for point in m:
    res.append([dist(c, point), point])

q1 = min(res)[1][0]
q2 = min(res)[1][1]

print(q1, q2)

# 7  23