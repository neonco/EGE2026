with open('26_28945.txt') as f:
    m = [[int(x) for x in s.split()] for s in f.readlines()[1:]]

m = [[start, dist, start+dist] for start, dist in m]

m = sorted(m, key=lambda x: x[2])
temp = m
print(m[:10])
res = []
while m:
    el = m[0]
    res.append(el)
    m = [x for x in m if x[0] >= el[2]]

print(len(res))
print(res[-2])
l = [x for x in temp if res[-2][2] <= x[0]]
print(l)