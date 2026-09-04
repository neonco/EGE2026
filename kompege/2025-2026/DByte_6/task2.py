for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not (x or y) or (y and z)) and w
                if f == 1:
                    print(z, w, y, x, f)

# zwyx