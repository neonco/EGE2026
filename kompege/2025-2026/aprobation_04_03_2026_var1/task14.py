from itertools import product

for n in product('012345', repeat=5):
    n = ''.join(n)
    d = int(n, 6)
    if d <= 2030:
        print(d, n)