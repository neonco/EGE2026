def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res.append(d)
            res.append(n // d)
    return sorted(set(res))


for n in range(1_350_050, 1_350_050+100):
    m = [d for d in f(n)[:-1] if d % 100 == 11 and d != 11]
    if m:
        print(n, m[0])

# 1350051 311
# 1350055 270011
# 1350062 511
# 1350063 40911
# 1350066 225011