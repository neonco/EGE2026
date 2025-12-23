# параметр A - 1 штука
# переменный x и y - 2 штука

pairs = []
for x in range(1, 501):
    for y in range(1, 501):
        pairs.append([x, y])

for a in range(1, 501):
    for x, y in pairs:
        f = (x < a) and (y < 3*a) or (2*x + y > 128)
        if f == 0:
            break
    else:
        print(a)

