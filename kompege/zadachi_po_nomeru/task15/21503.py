p = range(10, 40+1)
q = range(20, 50+1)

pairs = []
for x in range(-250, 300):
    for y in range(x+1, 300):
        pairs.append((x, y))

# print(len(pairs), pairs[:10])
res = []
for start, end in pairs:
    a = range(start, end+1)
    for x in range(-300, 400):
        f = not(x in p) or (not((x in q) and not(x in a)) or not(x in p))
        if not f:
            break
    else:
        res.append((end-start, start, end))

print(min(res))
# 20
