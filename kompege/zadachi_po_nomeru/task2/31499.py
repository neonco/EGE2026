for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (not (x != y) or not(not w or x)) or not z
                if f == 0:
                    print(y, x, z, w, f)

# yxzw

from itertools import product

for w, x, y, z in product(range(2), repeat=4):
    f = (not (x != y) or not (not w or x)) or not z
    if f == 0:
        print(y, x, z, w, f)

# yxzw
# Hello 7 class!