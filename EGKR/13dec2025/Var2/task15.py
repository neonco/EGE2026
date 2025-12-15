pairs = [(x, y) for x in range(-5, 600) for y in range(x+1, 600)]

p = range(225, 464+1)
q = range(140, 315+1)

for start, end in pairs:
    a = range(start, end+1)
    for x in range(-10, 700):
        f = not (x in p) or (not((x in q) and (x not in a)) or (x not in p))
        if not f:
            break
    else:
        if end - start < 91:
            print(start, end, len(a), end-start)

# [1, 10] math len = end - start  = 9
# python len = 10

# 90  [225, 315]