from itertools import product

for w, x, y, z in product(range(2), repeat=4):
    f = ((not w or not y) and (not y or x)) or (z and y)
    if f == 1:
        print(y, z, w, x, f)


# y, w, x, z
# y, w, z, x
# y, z, w, x
# y, z, x, w