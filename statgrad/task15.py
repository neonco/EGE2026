pairs = []
for x in range(1, 400):
    for y in range(1, 400):
        pairs.append([x, y])


for a in range(0, 400):
    for x, y in pairs:
        f = (y > a) or (152 != (2*y + 3*x)) or (a < x)
        if f == 0:
            break
    else:
        print(a)

# 30