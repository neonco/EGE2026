from math import prod
from itertools import product

def f(n):
    res = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

primes = [x for x in range(2, 30) if len(f(x)) == 2]
print(primes)

res = []
for r in range(3, 10):
    print(r)
    for pows in product(range(9), repeat=r):
        if list(pows) == sorted(pows, reverse=True):
            p = 1
            for prime, power in zip(primes[:r], pows):
                p *= prime**power
                if p > 10**11:
                    break
            c = prod(pow+1 for pow in pows)
            if p <= 10**11:
                res.append((c, p))

# print(len(res))
res =  sorted(res)[::-1]
print(res[:20])

# [(4032, 97772875200), <-
#  (4032, 97772875200),
#  (3840, 96376119840), <-
#  (3840, 83805321600),
#  (3840, 83805321600),
#  (3840, 80313433200),
#  (3600, 73329656400), <-
#  (3600, 73329656400),
#  (3584, 69837768000), <-
#  (3584, 69837768000),
#  (3584, 64250746560),
#  (3456, 93699005400), <-
#  (3456, 92626934400),
#  (3456, 92626934400),
#  (3456, 92626934400),
#  (3456, 85667662080),
#  (3456, 65181916800),
#  (3456, 65181916800),
#  (3456, 62853991200),
#  (3456, 62853991200)]
