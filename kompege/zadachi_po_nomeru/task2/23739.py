for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x or y) and not(y == z) and not w
                if f:
                    print(z, y, x, w, f)