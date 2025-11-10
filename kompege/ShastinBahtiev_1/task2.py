for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = z or (x == (not y or w))
                if f == 0:
                    print(y, z, w, x)