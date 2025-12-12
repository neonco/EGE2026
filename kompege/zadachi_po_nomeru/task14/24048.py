from string import digits, ascii_uppercase

d = dict()
for i, digit in enumerate(digits + ascii_uppercase):
    d[digit] = i
print(d)

def perevod(word, base):
    return sum([d[bukva] * base ** i for i, bukva in enumerate(word[::-1])])


for p in range(35, 100):
    a = perevod('KOT', p)
    b = perevod('GOLODNI', p)

    c = perevod('MEEOW', p) * perevod('100', p)

    res = (a + b == c - 20194023088)

    print(p, res, perevod('PURR', p))

# 1529685