with open('26_23208.txt') as f:
    m = [[int(x) for x in s.split()] for s in f.readlines()[1:]]

m = [[*x, i+1] for i, x in enumerate(m)]
m = sorted(m, key=lambda x: min(x[:2]))
shlif = []
kras = []
for a, b, i in m:
    if a < b:
        shlif.append(i)
    else:
        kras.append(i)

print(kras[-1], len(shlif))

# 503 478



