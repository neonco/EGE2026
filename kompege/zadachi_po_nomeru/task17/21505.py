with open('17_21505.txt') as file:
    m = [int(x) for x in file.readlines()]

l = max([x for x in m if len(str(x)) == 5 and x % 100 == 25])
# print(l)
# 49925

res = []
for a, b, c in zip(m, m[1:], m[2:]):
    if any([len(str(abs(x))) == 5 and abs(x) % 100 == 25 for x in (a, b, c)]):
        s = a*a + b*b + c*c
        if s <= l*l:
            print(a, b, c)
            res.append(s)

print(len(res), min(res))

# 3 1227276086
