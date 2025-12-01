def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

for n in range(1_000_000, 1_000_000 + 100):
    q = sum(f(n)[1:-1])
    if len(f(q)) == 2:
        print(n, q)

# 1000020 2201387
# 1000054 653641
# 1000056 1500143
# 1000066 532093
# 1000078 504289