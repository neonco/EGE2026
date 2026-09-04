with open('17_27629.txt') as f:
    m = [int(x) for x in f.readlines()]

l = max(x for x in m if 1000 <= abs(x) <= 9999 and x % 100 == 43)
# print(l)
# 9943

res = []
for pair in zip(m, m[1:]):
    if any(1000 <= abs(x) <= 9999 for x in pair):
        sq = sum(pair) ** 2
        if sq < l*l:
            res.append(sq)

print(len(res), max(res))
# 1218 98843364


