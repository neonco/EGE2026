with open('26_21424.txt') as f:
    m = [int(x) for x in f.readlines()[1:]]

m = sorted(m)[::-1]
res = [m[0]]
for box in m:
    if res[-1] - box >= 9:
        res.append(box)

print(len(res), res[-1])