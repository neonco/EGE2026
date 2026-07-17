from string import digits, ascii_lowercase

alph = digits + ascii_lowercase

for x in alph[:22]:
    a = f'12313{x}57'
    b = f'1{x}34561'
    a = int(a, 22)
    b = int(b, 22)
    s = a + b
    if s % 21 == 0:
        print(x, s // 21)

# 140914722