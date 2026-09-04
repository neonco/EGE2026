pairs = []
for start in range(-100, 300):
    for end in range(start+1, 300):
        pairs.append([start, end])

p = range(25, 64+1)
q = range(40, 115+1)
for start, end in pairs:
    a = range(start, end+1)
    for x in range(-100, 300):
        f = not(x in p) or (not ((x in q) and (x not in a)) or (x not in p))
        if f == 0:
            break
    else:
        if end - start < 25:
            print(end-start, start, end)

# 24