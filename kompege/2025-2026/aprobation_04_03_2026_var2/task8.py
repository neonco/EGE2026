from itertools import product

res = 0
for x in product('0123456', repeat=5):
    if x[0] != '0':
        if x.count('0') == 1:
            if x.count('1') <= 2:
                print(x)
                res += 1

print(res)

# 5100