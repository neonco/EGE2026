pairs = [(x, y) for x in range(487, 1000) for y in range(1, 1000)]

for a in range(0, 1000_000):
    for x, y in pairs:
        f = (x*y < a) or (5*x < y)
        if not f:
            break
    else:
        print(a)

# доделать
