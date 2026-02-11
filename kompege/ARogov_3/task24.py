from collections import Counter

with open('24.txt') as f:
    s = f.readline()

print(Counter(s))

s = s.replace('XYZY', 'XYZ  YZY')
for pair in ['XY', 'ZY']:
    s = s.replace(pair, 'AA')
for x in 'XYZ':
    s = s.replace(x, ' ')

s = s.split()
s = [len(x)//2 for x in s]
print(max(s))
print(s[:50])