with open('24_24240.txt') as f:
    s = f.readline()

print(len(s), set(s))

index = [i for i, symbol in enumerate(s) if symbol in '0123456789']

res = []
for x, y in zip(index, index[1:]):
    if s[x] == s[y]:
        res.append((y - x + 1, x))


print(sorted(res)[-2:])

# 5885703
