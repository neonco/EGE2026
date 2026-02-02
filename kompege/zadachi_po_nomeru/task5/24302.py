def f(n):
    res = ''
    a = '012'
    while  n > 0:
        res = res + a[n % 3]
        n =  n // 3
    return res[::-1]


res = []
for n in range(167, 1_000_000):
    t = f(n)
    # print(t)

    m = [int(digit) for digit in t]
    # '100' -> '1', '0', '0' -> 1, 0, 0 -> 1

    if sum(m) % 9 == 0:
        t = t + '2'
    else:
        t = t + f(sum(m) % 9)

    r = int(t, 3)
    res.append(r)

print(min(res))
# 647