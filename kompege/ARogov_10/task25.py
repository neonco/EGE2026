def f(n):
    res = set()
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)

k = 5_200_000
for n in range(k+1, k+2000):
    p = [x for x in f(n) if len(f(x)) == 2 and x != n]
    if p:
        m = p[0] + p[-1]
        if m > 50_000 and m % 100 == 26:
            # print(n, m, p)
            print(n, m)

# 5200105 1040026
# 5200369 226126
# 5200869 1733626
# 5201169 1733726
# 5201365 80026
