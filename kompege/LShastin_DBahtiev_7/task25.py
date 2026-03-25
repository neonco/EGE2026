p = [2]
for n in range(3, 100_000, 2):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            break
    else:
        p.append(n)

for n in range(2_000_000, 2_000_000+3000):
    temp = n
    m = []
    for d in p:
        while n % d == 0:
            n //= d
            m.append(d)
        if len(m) > 4:
            break
    if len(m) == 4 and len([x for x in m if x > 600]) >= 2:
        print(temp, m, m[0]*m[1]*m[2]*m[3])

# 2000156 743
# 2000524 773
# 2001212 739
# 2001508 757
# 2001548 811
