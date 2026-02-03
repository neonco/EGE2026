from itertools import product, repeat

for w, x, y, z in product(range(2), repeat=4):
    f = ((not w or z) == (not x or not y)) and (x or z)
    if f == 1:
        print(z, x, y, w, f)

# zxyw