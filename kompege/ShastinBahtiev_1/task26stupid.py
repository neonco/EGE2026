with open('26 (2).txt') as file:
    m = file.readlines()[1:]

m = [x.split() for x in m]
m = [[int(a), int(b)] for a, b in m]
m = m

res = []
c = 0

for t in range(0, 1441):
    for start, end in m:
        if start == t:
            c += 1
        if end == t:
            c -= 1
    res.append([c, t])
print(sorted(res))
