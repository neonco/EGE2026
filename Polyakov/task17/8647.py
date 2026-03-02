with open('17-447.txt') as f:
    m = [int(x) for x in f.readlines()]

lim = min(x for x in m if 1000 <= x <= 9999)
print(lim)

for n in range(1000, 10000):
    if n in m:
        print(n)
        break

res = []
for trio in zip(m, m[1:], m[2:]):
    if sum([x % 2 == 0 for x in trio if len(str(abs(x))) == 3]) >= 2:
        if sum(trio) >= lim:
            res.append(sum(trio))

print(len(res), min(res))
