def f(n):
    res = [d for d in range(1, int(n**0.5)+1) if n % d == 0]
    res += [n//d for d in res if n // d != d][::-1]
    return res

for n in range(13_200_000, 13_200_000+1000):
    p = [d for d in f(n) if len(f(d)) == 2]
    m = 0
    if len(p) >= 2:
        m = p[0] + p[-1]
    if m > 30_000 and m % 100 == 55:
        print(n, m)

# 13200024 32355
# 13200106 6600055
# 13200172 106455
# 13200356 253855
# 13200602 388255
# 13200918 2200155
# 13200938 38155