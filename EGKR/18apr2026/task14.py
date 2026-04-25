from string import digits, ascii_uppercase

alph = digits + ascii_uppercase
alph = alph[:23]

for x in alph:
    res = int(f'761{x}035', 23) + int(f'338{x}932', 23)
    if res % 22 == 0:
        print(x, res // 22)

# 70045642