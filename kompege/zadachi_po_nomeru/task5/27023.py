# print(bin(2002)[2:])
#
# # 11    00
# # 10    01
# # 01    10
#
# print(int('11110100', 2))

# 2002

for n in range(1, 400):
    b = bin(n)[2:]
    s = b.count('1')
    if s % 3 == 0:
        b = '11' + b + '00'
    if s % 3 == 1:
        b = '10' + b + '01'
    if s % 3 == 2:
        b = '01' + b + '10'
    r = int(b, base=2)
    if r in range(2001, 2010):
        print(n, r)


