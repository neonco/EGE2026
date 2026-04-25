from collections import Counter
from pprint import pprint

with open('24_26078.txt') as f:
    s = f.readline()

l = len(s)
# pprint(Counter(s))
s = s.replace('W', ' W')
s = 'W' + s
s = s.split()
res = []
for i in range(0, len(s)):
    cur = ''.join(s[i:i+91])[1:]
    if cur.count('2025') >= 110:
        res.append(cur)

res = sorted(res, key=len)
for x in res[:10]:
    print(len(x), x.count('W'), x.count('2025'), x)

# 780
