from math import ceil

def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))


start = ceil(123456789**0.5)
end = int(223456789**0.5)

for x in range(start, end+1):
    n = x * x
    if len(f(n)) == 5:
        print(n, f(n)[-2])


# 131079601 1225043
# 141158161 1295029
# 163047361 1442897



