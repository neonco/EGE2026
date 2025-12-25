def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

def kar(n):
    res = []
    factor = [d for d in f(n) if len(f(d)) == 2]
    for d in factor:
        c = 0
        while n % d == 0:
            c += 1
            n //= d
            res.append(d**c)
    return res


limit = 13_475_124
for n in range(limit, limit + 200000):
    m = kar(n)
    if len(m) == 5:
        if m == [x for x in m if '5' in str(x)]:
            print(n, max(m))

# 13476875 21563
# 13480625 21569
# 13485625 21577
# 13491875 21587
# 13493125 21589