with open('24.txt') as file:
    s = file.readline()

t = s.split('A')

t = [f'{'1'*len(x)} {'1'*len(x)}' if len(x) < 2 else x for x in t]
t = 'A'.join(t)

t = t.split()
t = [x for x in t if x.count('A') >= 320]
print(len(t))
res = []
for s in t:
    if 'A' not in s[:2]:
        s = 'A' + s
    if 'A' not in s[-2:]:
        s = s + 'A'
    m = [j for j, x in enumerate(s) if x == 'A']
    for a, b in zip(m, m[321:]):
        g = s[a:b+1]
        print(g.count('A'), g[:5], g[-5:])
        res.append(len(g)-2)

print(max(res))
# 80474