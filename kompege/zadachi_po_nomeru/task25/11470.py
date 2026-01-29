from math import prod
from itertools import product

def f(n):
    res = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

# nums = [1, 2, 3, 5, 7, 11, 13]
# for x in product(nums, repeat=10):
#     num = prod(x)
#     print(num, len(f(num)))
# piska