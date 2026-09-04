from pprint import pprint

with open('26_23765.txt') as f:
    m = f.readlines()[1:]

m = [[int(x) for x in y.split()]+[i+1] for i, y in enumerate(m)]
m = sorted(m)

pprint(m)

res1 = m[-1][-1]
res2 = len([[x, y, i] for x, y, i in m if y < x])-1
print(res1, res2)

# 563 444