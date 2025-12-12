from string import digits, ascii_uppercase

def f(s, base):
    alph = digits+ascii_uppercase
    return sum([alph.index(d) * base ** i for i, d in enumerate(s[::-1])])

for x in range(10):
    left = f('SLADOST', 36) + f('GADOST', 100+x)
    right = f('HALLOWEEN', 50-x) - 166729861760449
    if left == right:
        print(x, f('GADOST', 13+100*x))

# 5687311088501708





