file = open('17_24892.txt').readlines()

m = [int(el) for el in file]
print(m[:10])

limit = max([el for el in m if -9999 <= el <= -1000 and el % 9 == 0])
print(limit)
# -1377


res = []
for i in range(len(m)-1):
    p = m[i] * m[i+1]
    s = m[i] + m[i+1]
    if p == 0:
        if s < 0 and s > limit:
            res.append(m[i] * m[i] + m[i+1] * m[i+1])
    elif p < 0:
        if s > limit:
            res.append(m[i] * m[i] + m[i+1] * m[i+1])

print(len(res), min(res))
