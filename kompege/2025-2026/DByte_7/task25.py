def f(n):
    res = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)

k = 1_000_000
for n in range(k+1, k+100):
    d = f(n)[1:-1]
    q = sum(d)
    if len(f(q)) == 2:
        print(n, q)

# 1000020 2201387
# 1000054 653641
# 1000056 1500143
# 1000066 532093
# 1000078 504289