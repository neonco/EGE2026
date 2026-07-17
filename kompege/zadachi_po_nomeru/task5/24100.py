def f(n):
    res = ''
    a = '012'
    while n > 0:
        res += a[n % 3]
        n //= 3
    return res[::-1]

for n in range(1, 10000):
    t = f(n)
    if n % 5 == 0:
        t = t + t[-2:]
    else:
        t = t + f((n % 5) * 7)
    res = int(t, base=3)
    if res <= 273:
        print(n, res)