from collections import Counter

with open('24.txt') as f:
    s = f.readline()[:-1]

print(Counter(s))
alph = set(s)
for _ in range(5):
    for x in alph:
        s = s.replace(x+x, x+' '+x)

s = s.split()
s = [len(x) for x in s]
print(max(s))

print(s[:30])

# 170
