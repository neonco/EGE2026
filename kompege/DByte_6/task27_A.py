from math import dist

with open('27_A_27035.txt') as f:
    m = [[float(c) for c in p.replace(',', '.').split()] for p in f.readlines()]

m = [[i, p] for i, p in enumerate(m)]

for a in m:
    for b in m:
        if dist(a[1], b[1]) <= 10:
            a[0] = b[0] = min(a[0], b[0])

cl = [i for i, p in m]

# for i, p in m:
#     print(i, p)

print(set(cl))

c1 = [p for i, p in m if i == 0]
c2 = [p for i, p in m if i == 102]

centr1 = min(c1, key=lambda x: sum([dist(x, p) for p in c1]))
centr2 = min(c2, key=lambda x: sum([dist(x, p) for p in c2]))

resx = int((centr2[0] - centr1[0]) * 10_000)
resy = int((centr2[1] - centr1[1]) * 10_000)
print(resx, resy)
