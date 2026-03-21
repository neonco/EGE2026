for n in range(4, 100):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + b[-3:]
    else:
        b = '1' + b + '01'
    r = int(b, base=2)
    print(n, abs(r-155), r)

# 20