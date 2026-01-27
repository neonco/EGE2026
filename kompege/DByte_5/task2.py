from itertools import product

for x, y, z, w in product(range(2), repeat=4):
    f = w and ((y and z) or not(x or y))
    if f == 1:
        print(y, x, z, w)

# yxzw