# from string import ascii_lowercase
#
# a = '0123456789' + ascii_lowercase
# a = a[:23]

a = '0123456789ABCDEFGHIJKLM'
print(len(a))
for x in a:
    a = f'90{x}5F42'
    b = f'{x}4C82G1'
    res = int(a, 23) + int(b, 23)
    print(res, res/22)

# 95598761