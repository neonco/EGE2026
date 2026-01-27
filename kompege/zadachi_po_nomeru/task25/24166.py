def f(n):
    lim = int(n**0.5) + 1
    res = []
    for d in range(1, lim):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

def kar(n):
    res = []
    factor = [d for d in f(n) if len(f(d)) == 2]
    for d in factor:
        while n % d == 0:
            n //= d
            res.append(d)
    return res

for n in range(7_305_678+1, 7_305_678+1_000):
    if len(kar(n)) == 4:
        s = str(sum(kar(n)))
        if s == s[::-1]:
            print(n, s)


# 7305747 2002
# 7305818 16561
# 7305986 545
# 7306057 696
# 7306059 606