from collections import Counter

with open('24_11_15.txt') as f:
    s = f.readline()[:-1]

print(Counter(s))

# s = 'Y' + s + 'Y'
s = s.replace('Y', ' Y')
s = s.split()

s = [len(x) for x in s]

res = []
for i in range(len(s)-99):
    res.append(sum(s[i:i+99])+1)

print(min(res))
print(s[:100])

# 3756