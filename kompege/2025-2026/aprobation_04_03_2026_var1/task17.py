with open('17_27629.txt') as file:
    m = [int(x) for x in file.readlines()]

print(len(m))

l = max(x for x in m if 1000 <= x <= 9999 and x % 100 == 43)
print(l)
# 9943

res = []
for a, b in zip(m, m[1:]):
    if 1000 <= abs(a) <= 9999 or 1000 <= abs(b) <= 9999:
        sq = (a+b) ** 2
        if sq < l*l:
            res.append(sq)

print(len(res), max(res), l*l)

# 1218 98843364