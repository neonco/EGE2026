def f(n):
    res = set()
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res.add(d)
            res.add(n//d)
    return sorted(res)

x = 7_800_000
for n in range(x+1, x+3000):
    pr = [x for x in f(n) if len(f(x)) == 2]
    k = len(pr)
    if pr[-1] != n:
        m = pr[0] + pr[-1]
        if m % 100 == 63 and m % k == 0:
            # print(n, m, pr, k)
            print(n, m)

# 7800610 780063
# 7801042 8463
# 7801312 1863
# 7801916 8163
# 7802032 69663