res = 0
for a in range(1, 11_111+1):
    for x in range(1, 25_000):
        f = (not (a % x == 0) or (x == a) or (x == 1))
        if f == 0:
            break
    else:
        res += 1

print(res)