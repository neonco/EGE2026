pairs = []
for x in range(1, 400):
    for y in range(1, 400):
        pairs.append([x, y])


for a in range(1, 500):
    for x, y in pairs:
        f = (x*y < a) or (y >= x) or (x > 12)
        if f == False:
            break
    else:
        print(a)

