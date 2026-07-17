for n in range(19, 1000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, base=2)
    if r <= 100:
        print(n, r)

# 84