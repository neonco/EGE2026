from collections import Counter

with open('24_29354.txt') as file:
    s = file.readline().strip()

s = s
print(len(s))
# print(Counter(s))

ind = []
res = 0

for i in range(len(s)-1):
    if s[i]+s[i+1] == 'BC':
        ind.append(i)

for a, b in zip(ind, ind[191:]):
    res = max(res, b-a)

print(res)

# 2287