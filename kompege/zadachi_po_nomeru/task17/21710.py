pairs = []
for x in range(-100, 301):
    for y in range(x+1, 301):
        pairs.append([x, y])

b = range(36, 75+1)
c = range(60, 110+1)

for start, end in pairs:
    a = range(start, end+1)
    for x in range(-100, 400):
        f = not not(x in a) or ((x in b) == (x in c))
        if f == 0:
            break
    else:
        if end - start < 76:
            print(a, end - start)

# 74