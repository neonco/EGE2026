with open('24_28943.txt') as f:
    s = f.readline()

print(set(s))
print(len(s))

gl = 'AEIOUY'
for x in gl:
    s = s.replace(x, 'A')
c = ''
res = 100000000000000000000000000000

for i, bukva in enumerate(s):

    if i % 10_000 == 0:
        print(i)


    c += bukva
    while (c[-1] == 'A') and (c.count('20') == 26) and (c.count('A') == 1):
        res = min(res, len(c))
        c = c[1:]
    while c.count('20') > 26:
        c = c[1:]

print(res)

# 58