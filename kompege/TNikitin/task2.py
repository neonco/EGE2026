from itertools import product, repeat

for a, b, c, d in product(range(2), repeat=4):
    f = (not((d or not b) and ((a and b) or c)) or (not d or (a or not c))) and ((not b or c) == (d and not a))
    if f:
        print(c, b, d, a, f)

# cbda