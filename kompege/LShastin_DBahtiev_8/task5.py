from itertools import product
from math import prod

for x in product([0,1,2,3,4,5,6,7,8,9], repeat=6):
    if x[0] != 0:
        s = sum(x)
        b1 = sum(sorted(x)[1:-1])
        b2 = prod(d for d in x if d != 0) - 2*s
        res = f'{max(b1, b2)}{min(b1, b2)}'
        if res == '26714':
            print(x, s, b1, b2, res)

# (9, 7, 5, 1, 1, 1) 24 14 267 26714