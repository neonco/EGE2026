def f(n):
    res = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

for n in range(1_475_000-1, 1_475_000-100, -1):
    s = sum([d for d in f(n)[:-1] if len(f(d)) == 2])
    if s < 42_000 and s % 6 == 0 and s != 0:
        print(n, s)

# m = []
# for d in f(n)[:-1]:
#     if len(f(d)) == 2:
#         m.append(d)
# s = sum(m)
