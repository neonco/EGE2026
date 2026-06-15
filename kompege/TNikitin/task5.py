from itertools import combinations

fib = [1, 2]
for _ in range(70):
    fib.append(sum(fib[-2:]))

def tuda(n):
    res = []
    for d in [x for x in fib[::-1] if x <= n]:
        i = (1 if d <= n else 0)
        res.append(i)
        n = n - d*i
    return res

def suda(posled):
    res = 0
    for i, x in zip(posled[::-1], fib):
        res += i * x
    return res

duo = combinations(range(2, 60), r=2)
trio = combinations(range(2, 60), r=3)
duo = [x for x in duo if (x[1] - x[0]) > 1]
trio = [x for x in trio if ((x[2] - x[1]) > 1) and ((x[1] - x[0]) > 1)]

m = []
for comb in duo+trio:
    num = [1] + [0]*59
    for i in comb:
        num[i] = 1
    m.append(num)

print(len(m))