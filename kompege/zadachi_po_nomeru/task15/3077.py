pairs = []
for x in range(0, 1000):
    for y in range(0, 1000):
        pairs.append([x, y])

for a in range(0, 2000000):
    for x, y in pairs:
        f = ((680*y + 256*x) < a) or ((5*x + 3*y) > 11111)
        if f == 0:
            break
    else:
        print(a, x, y)