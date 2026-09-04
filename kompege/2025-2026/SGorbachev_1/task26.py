from collections import Counter

with open('26.txt') as f:
    m = f.readlines()

n = int(m[0])
m = m[1:]
m = list(set(m))
m = [el.split() for el in m]
m = [int(a) for a, b in m]

print(Counter(m))
# 33934: 19 без set
# 46264: 5  с set

