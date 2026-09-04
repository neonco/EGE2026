from collections import defaultdict

with open('26.txt') as file:
    m = file.readlines()[1:]

m = [[int(x) for x in s.split()] for s in m]
m = sorted(m, reverse=True)

d = defaultdict(list)
for o, p, misl in m:
    d[(o, p)].append(misl)

ost = 0
for k,v in d.items():
    if len(v) > 1:
        ost += sum(v[1:])
    d[k] = v[0]

obl = defaultdict(list)
for k,v in d.items():
    obl[k[0]].append(v)

obl = [(sum(v),k) for k,v in obl.items()]
obl = sorted(obl)
print(obl[-10:])

print(obl[-1][1], ost)

# 824 10992169



