pairs = []
for x in range(285, 1000):
    for y in range(x+123, 1000):
        pairs += [(x, y)]

q = range(285, 714+1)
for j in range(108, 1000):
    p = range(107, j+1)
    for start, end in pairs:
        a = range(start, end+1)
        for x in range(-100, 1100):
            f = (x not in p) or (not((x in q) and (x not in a)) or (x not in p))
            if not f:
                break
        else:
            if end-start == 123:
                print(j, start, end)
                break

# 408