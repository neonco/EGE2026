from string import digits, ascii_uppercase

def f(n, base):
    a = digits + ascii_uppercase
    s = ''
    while n > 0:
        s = a[n % base] + s
        n = n // base
    return s

for n in range(1, 10):
    t = f(n, 3)
    if n % 3 == 0:
        t = '1' + t + '02'
    else:
        t = t + f((n % 3) * 5, 3)

    res = int(t, 3)
    print(n, res)

# 8 226