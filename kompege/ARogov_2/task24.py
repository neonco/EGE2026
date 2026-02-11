from collections import Counter

with open('24.txt') as f:
    s = f.readline()[:-1]

print(len(s))
print(Counter(s))

for x in 'AEU':
    s = s.replace(x, 'A')

for x in 'BCDF':
    s = s.replace(x, 'B')

s = s.replace('BAB', 'YYY')
for _ in range(10):
    s = s.replace('BAY', 'YYY Y')
    s = s.replace('YAB', 'Y YYY')
s = s.replace('YYY', ' YYY')
s = s.split()
# s = [len(x) for x in s]

res = []
for a, b, c in zip(s, s[1:], s[2:]):
    m = len(a+b+c)-1+2
    if m == 117:
        print(a, b, c)
    res.append(m)

print(max(res))

# 108

print(s[:10])



