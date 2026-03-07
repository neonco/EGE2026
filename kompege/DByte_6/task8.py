from itertools import product

a = '0123456789ABCDEF'

print(16**4)

res = 0
for w in product(a, repeat=4):
    w = ''.join(w)
    if w.count('1') + w.count('4') + w.count('9') == 2:
        if w[0] != w[1] and w[1] != w[2] and w[2] != w[3]:
            if w[0] != '0' and w[-1] in '08':
                print(w)
                res += 1
print(res)