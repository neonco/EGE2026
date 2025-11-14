pairs = []
for s in range(-100, 700):
    for e in range(s+1, 700):
        pairs.append([s, e])


p = range(257, 356+1)
q = range(5, 600+1)
r = range(59, 228+1)

for s, e in pairs:
    a = range(s, e+1)
    for x in range(-200, 800):
        f = (not (x in r) or (x in a)) or (not(not(x%3==0) or (x in p)) or (not(x in q) or (x in a)))
        if not f:
            break
    else:
        print(s, e, len(a)-1)
print(227-59)
