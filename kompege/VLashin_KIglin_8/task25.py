p = []
for n in range(3, 4_000_000, 2):
    if '3' in str(n):
        for d in range(2, int(n ** 0.5)+1):
            if n % d == 0:
                break
        else:
            p.append(n)

l = 6_999_123
for temp in range(l+1, l+1000):
    n = temp
    m = []
    for d in p:
        if n % d == 0:
            n //= d
            m.append(d)
    if n == 1:
        print(temp, n, m, len(m))

# 6999127 132059
# 6999161 538397
# 6999177 2333059
# 6999187 538399
# 6999197 5003
# 6999207 2333069