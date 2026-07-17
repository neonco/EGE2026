from math import dist

with open('27_B.txt') as file:
    m = [x.split() for x in file.readlines()]

m = [[i, float(x), float(y)] for i, (x, y) in enumerate(m)]

# print(m)
gap = 1
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1:], m[j][1:]) <= gap:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

ind =  [i for i, *p in m]
print(set(ind))

m0 = [p for i, *p in m if i == 0]
m1 = [p for i, *p in m if i == 1]
m2 = [p for i, *p in m if i == 12]

print(len(m0), len(m1), len(m2), len(m))
print(len(m0) + len(m1) + len(m2), len(m))

anticentr0 = max(m0, key=lambda p: sum([dist(p, q) for q in m0]))
anticentr1 = max(m1, key=lambda p: sum([dist(p, q) for q in m1]))
anticentr2 = max(m2, key=lambda p: sum([dist(p, q) for q in m2]))
print(anticentr0, anticentr1, anticentr2)

q1 = (len(m0) + len(m2)) * 10000

d0 = dist(anticentr0, anticentr1)
d1 = dist(anticentr1, anticentr2)
d2 = dist(anticentr0, anticentr2)

q2 = int(min(d0, d1, d2)*10000)

print(q1, q2)

# 5030000 73416
