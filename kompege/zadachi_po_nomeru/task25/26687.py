def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))


# print(f(100))
# [1, 2, 4, 5, 10, 20, 25, 50, 100]
#  1  1  1  1  1  ...
#     2  2  5  2
#        4     5
#              10

start = 89427150
for n in range(start+1, start+40000):
    divs = f(n)
    pdivs = [d for d in divs if len(f(d)) == 2]
    # print(pdivs)
    x = n
    m = []
    for pd in pdivs:
        count = 0
        while x % pd == 0:
            count = count + 1
            x = x // pd
        m.append(count)
    if sum(m) == 8 and m[0] == 1 and [x for x in m if x > 1] == [2, 2]:
        print(n, pdivs, m)


# 89439210 [2, 3, 5, 7, 17, 1193] [1, 2, 1, 2, 1, 1]
# 89439570 [2, 3, 5, 11, 43, 191] [1, 2, 1, 2, 1, 1]
# 89442150 [2, 3, 5, 7, 43, 283] [1, 1, 2, 2, 1, 1]
# 89446266 [2, 3, 7, 13, 29, 269] [1, 2, 2, 1, 1, 1]
# 89448390 [2, 3, 5, 17, 19, 181] [1, 2, 1, 2, 1, 1]
# 89450550 [2, 3, 5, 7, 73, 389] [1, 2, 2, 1, 1, 1]
# 89451450 [2, 3, 5, 11, 17, 1063] [1, 2, 2, 1, 1, 1]
















# 100 // 2 = 50
# 50 // 2 = 25
# 25 // 5 = 5
# 5 // 5 = 1
# count = 0
# pdivs = [2, 5]
# x = 1000
# for pd in pdivs:
#     while x % pd == 0:
#         count = count + 1
#         x = x // pd
#         print(x)
# print(count)

