with open('17-449.txt') as f:
    m = [int(x) for x in f.readlines()]

limit = max([x for x in m if '38' in str(x)])
print(limit)

res = []
for a, b, c in zip(m, m[1:], m[2:]):
    word = f'{a}__{b}__{c}'
    if word.count('-') == 2:
        s = a + b + c
        if s <= limit:
            res.append(s)

print(len(res))
print(max([x for x in res if str(x)[:2] == '38']))

# 3009
# 38806

