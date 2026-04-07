from math import dist

with open('27_A.txt') as file:
    m = [x.split() for x in file.readlines()]

m = [[i, float(x), float(y)] for i, (x, y) in enumerate(m)]

# print(m)
gap = 1
for i in range(len(m)):
    for j in range(len(m)):
        if dist(m[i][1:], m[j][1:]) <= gap:
            m[i][0] = m[j][0] = min(m[i][0], m[j][0])

# for i, *p in m:
#     print(i)

m0 = [p for i, *p in m if i == 0]
m1 = [p for i, *p in m if i == 1]
print(len(m0), len(m1), len(m))

anticentr0 = max(m0, key=lambda p: sum([dist(p, q) for q in m0]))
anticentr1 = max(m1, key=lambda p: sum([dist(p, q) for q in m1]))
print(anticentr0, anticentr1)

nearest0 = min([dist(anticentr0, p) for p in m0 if p != anticentr0])
nearest1 = min([dist(anticentr1, p) for p in m1 if p != anticentr1])

p1 = int(min(nearest0, nearest1) * 10000)
temp = [dist(anticentr0, p) for p in m1]
p2 = int(sum(temp)/len(temp) * 10000)
print(p1, p2)

# 3543 137509
