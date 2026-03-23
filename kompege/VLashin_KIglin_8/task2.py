from itertools import product

for w, x, y, z in product(range(2), repeat=4):
    f = not(x and z and not y) and not(w and x) and not(not(y or x) == w)
    if f:
        print(x, z, w, y, f)


# xzwy