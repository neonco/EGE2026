def f(n):
    res = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))


for n in range(700_000+1, 700_000+100_000):
    s = f(n)
    d = s[1]
    pattern = [d**i for i in range(len(s))]
    if s == pattern and len(s) > 2:
        print(n, d)


