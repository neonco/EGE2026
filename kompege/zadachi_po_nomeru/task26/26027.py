with open('26_26027.txt') as f:
    m = f.readlines()[1:]

m = [[int(x) for x in s.split()] for s in m]
m = [[*x, i+1] for i, x in enumerate(m)]

spok = [[a, b, i] for a, b, i in m if a < b]
prazdn = [[a, b, i] for a, b, i in m if b < a]


spok = sorted(spok, key=lambda x:(x[0], x[1]))
prazdn = sorted(prazdn, key=lambda x:(x[1], x[0]))

print(spok[:5])
print(prazdn[-5:])

# 402 (индекс первого из спокойных)
# 775 (индекс последнего из праздничных)
