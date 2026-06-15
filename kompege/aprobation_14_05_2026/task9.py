from pprint import pprint

with open('09_29962.txt') as f:
    m = f.readlines()

m = [[int(x) for x in s.split()] for s in m]
m = [sorted(s) for s in m]
# pprint(m)
for i, s in enumerate(m):
    ne_pov = [x for x in s if s.count(x) == 1]
    povtor = [x for x in s if s.count(x) == 3]
    if len(ne_pov) == 4 and len(povtor) == 3:
        if sum(ne_pov) / 4 > povtor[0]:
            print(i+1, s)

# 13609