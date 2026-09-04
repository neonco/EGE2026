for n in range(1000):

    b = f'{n:b}'
    if len([x for x in b.split('0') if len(x) in (2, 3)]) == 1:
        b = b + '0'
        b = '10' + b[2:]
    else:
        b = b + '1'
        b = '11' + b[2:]
    r = int(b, base=2)
    if 0 <= 1500-r < 10:
        print(n, b, r)

# 746
