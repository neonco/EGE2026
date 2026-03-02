with open('17-449.txt') as f:
    m = [int(s) for s in f.readlines()]

l = max(x for x in m if str(x)[:2] == '45')
print(l)

res = []
for a, b, c in zip(m, m[1:], m[2:]):
    s = a + b + c
    if f'{a}_{b}_{c}'.count('-') == 1:
        if s >= l:
            res.append(s)

print(len(res), min(x for x in res if str(x)[-2:] == '45'))