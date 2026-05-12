with open('24_28765.txt') as f:
    s = f.readline().strip()

current = ''
res = 0
print(len(s))

for i, symbol in enumerate(s):
    if i % 10_000 == 0:
        print(i)

    current += symbol
    while current.count('BC') > 180:
        current = current[1:]
    if current.count('BC') <= 180:
        res = max(res, len(current))

print(res)


# 38442