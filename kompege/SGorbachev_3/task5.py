def f(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n //= 5
    return s[::-1]

ans = 0
for n in range(1, 10_001):
    t = f(n)
    if sum(int(digit) for digit in t) % 2 == 0:
        t = t + '02'
        t = '42' + t[2:]

    if sum(int(digit) for digit in t) % 2 == 0:
        t = t + '02'
        t = '42' + t[2:]
    res = int(t, base=5)
    if res % 2 == 0:
        ans = max(res, ans)


print(f(10_000))
print(int('4244440202', base=5))
print(ans)

# 8983802