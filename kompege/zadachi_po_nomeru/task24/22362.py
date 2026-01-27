with open('24_22362.txt') as f:
    s = f.readline()

# print(set(s))

s_new = [x if x in '0123456789AB' else ' ' for x in s]
s_new = ''.join(s_new)

# print(s[:20])
# print(s_new[:20])
#
m = s_new.split()
# print(m[:20])
m = [x.lstrip('0') if len(x) > 1 else x for x in m if int(x, 12) % 3 == 0]
l = len(max(m, key=len))
print(l)
# длина 109
m = [x for x in m if len(x) == l]
# 1302691704385040825176930372864051902714635890010578436290346801792507245310689061528734900654720391800070293
pattern = '1302691704385040825176930372864051902714635890010578436290346801792507245310689061528734900654720391800070293'
print(s.find(pattern))

# 6817770


