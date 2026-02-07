with open('17_25356.txt') as f:
    m = [int(x) for x in f.readlines()]

l = max([x for x in m if x % 100 == 30])
print(l)
# 98530

res = []
for trio in zip(m, m[1:], m[2:]):
    t = [1000 <= abs(x) <= 9999 for x in trio]
    if sum(t) == 0:
        if sum(trio) > l:
            res.append(sum(trio))

print(len(res), max(res))

# 1032 285423

