from itertools import product, repeat

for w, x, y, z in product(range(2), repeat=4):
    f = (not(x or y) or z) or (y == w) or z
    if not f:
        print(w, y, x, z, f)

# wyxz