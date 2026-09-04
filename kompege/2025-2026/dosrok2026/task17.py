with open('17_28762.txt') as f:
    m = [int(x) for x in f.readlines()]

k = min(x for x in m if x % 23 == 0)
print(k)
# 184

res = []
# for a, b in zip(m, m[1:]):
#     if a % k == 0 or b % k == 0:
#         res.append(a+b)

for i in range(len(m)-1):
    a = m[i]
    b = m[i+1]
    if a % k == 0 or b % k == 0:
        res.append(a+b)

print(len(res), max(res))
# 113 168437