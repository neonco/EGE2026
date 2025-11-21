def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res.append(d)
            res.append(n // d)
    return sorted(set(res))


for n in range(6_200_001, 6_200_001+100_000):
    dels = f(n)
    # print(dels)
    prime_dels = [x for x in dels if len(f(x)) == 2]
    # print(prime_dels)
    m = prime_dels[0] + prime_dels[-1]
    if m > 70_000:
        if str(m) == str(m)[::-1]:
            print(n, m)