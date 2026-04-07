from collections import Counter
from collections import defaultdict

with open('26_22168.txt') as file:
    m = [[int(y) for y in x.split()] for x in file.readlines()[1:]]

# print(len(m), len(set([tuple(x) for x in m])))
# print(Counter([tuple(x) for x in m]))
# 13 повторов

d = defaultdict(set)
for id, task in m:
    if task % 2 == 0:
        d[id].add(task)

d = {k:len(v) for k,v in d.items()}
print(max(d.values()))
d = {k:v for k,v in d.items() if v == 21}
print(d)

# 271802 21

