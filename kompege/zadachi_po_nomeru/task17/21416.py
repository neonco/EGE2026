with open('17_21416.txt') as f:
    m = [int(x) for x in f.readlines()]


s = sum([x for x in m if x < 0])
print(s)
# -38042420

res = []
for trio in zip(m, m[1:], m[2:]):
    p = max(trio) * min(trio)
    if p > s:
        res.append(sum(trio))

print(len(res), abs(max(res)))

# 10007 7953
