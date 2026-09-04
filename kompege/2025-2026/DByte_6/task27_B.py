from math import dist

with open('27_B_27035.txt') as f:
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
c2 = [p for i, p in m if i == 203]
c3 = [p for i, p in m if i == 453]
print(len(c1), len(c2), len(c3))

centr1 = min(c1, key=lambda x: sum([dist(x, p) for p in c1]))
centr2 = min(c2, key=lambda x: sum([dist(x, p) for p in c2]))
centr3 = min(c3, key=lambda x: sum([dist(x, p) for p in c3]))

c1 = [[sum([dist(x, p) for p in c1]) / (len(c1)-1), x] for x in c1]
c2 = [[sum([dist(x, p) for p in c2]) / (len(c2)-1), x] for x in c2]
c3 = [[sum([dist(x, p) for p in c3]) / (len(c3)-1), x] for x in c3]

print(int(min(c1)[0]*10_000))
print(int(min(c3)[0]*10_000))
# 47556
# 72438