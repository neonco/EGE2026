from collections import defaultdict
from pprint import pprint

with open('26_29805.txt') as file:
    m = file.readlines()[1:]

m = [(int(x) for x in s.split()) for s in m]
print(len(m), len(set(m)))

d = defaultdict(list)
for stud, task in m:
    if task % 2 == 0:
        d[stud] += [task]

temp = sorted(d, key=lambda x: len(set(d[x])), reverse=True)
res = [[stud, d[stud], len(set(d[stud]))] for stud in temp]
pprint(res[:10])

# 271802 21