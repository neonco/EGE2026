for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not (not y or w) or x) or not z
                if f == 0:
                    print(z, y, w, x, f)

# zywx