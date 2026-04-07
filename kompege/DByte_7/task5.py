from string import digits

def f(n):
    res = ''
    while n > 0:
        res += digits[n % 5]
        n //= 5
    return res[::-1]

for n in range(50, 100+1):
    p = f(n)

    if n % 5 == 0:
        p = p[0] + p + p[-1]
    else:
        s = sum(int(x) for x in p)
        p = p + f(s)

    r = int(p, 5)
    if r % 5 == 0:
        print(n, r)


# 3000
