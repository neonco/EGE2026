with open('26_23765.txt') as f:
    m = f.readlines()[1:]

m = [[int(x) for x in s.split()]+[i+1] for i, s in enumerate(m)]

hran = [[a, b, i] for a, b, i in m if a < b]
godn = [[a, b, i] for a, b, i in m if a > b]

godn = sorted(godn, key=lambda x: (x[1], x[0]))

print(godn[-5:], len(godn)-1)

# 564 444