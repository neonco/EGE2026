from itertools import product

p = product(sorted('КАЛМБУР', reverse=True), repeat=7)
for i, x in enumerate(p):
    x = ''.join(x)
    if (i+1) % 2 == 1:
        if x[0] not in 'АМ':
            if x.count('Р') >= 3:
                print(i+1, x)

# 705609