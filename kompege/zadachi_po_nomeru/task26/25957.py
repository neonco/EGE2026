with open('26.txt') as file:
    m = [int(x) for x in file.readlines()[1:]]

m = sorted(m)
k = 100_000
res = []
ind_first_avg = 500113
t = m[ind_first_avg-500:ind_first_avg+500]
for i in range(k):
    if i % 100 == 0:
        print(i)
    avg = (m[i] + m[-1-i]) // 2
    # print(avg in m)
    # print(avg)
    for l, r in zip(t, t[1:]):
        if r == avg:
            res += [r, r]
            break
        elif r > avg:
            res += [l, r]
            break

# print(len(res), k*2)

print(sum(res))
print(max([res.count(x), x] for x in set(res)))

# 999834637071 4999341

# r = [r-l for l, r in zip(m, m[1:])]
# print(sum(r[:len(r)//2]), sum(r[len(r)//2:]), sum(r))
# print(sum(r[:10]), sum(r[-10:]))