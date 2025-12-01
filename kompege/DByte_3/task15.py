p = range(14, 42+1)
q = range(25, 96+1)

pairs = []
for start in range(-100, 400):
    for end in range(start+1, 400):
        pairs += [(start, end)]

for start, end in pairs:
    a = range(start, end+1)
    for x in range(-100, 400):
        f = not((not(x in p) or (x in a)) and (x in q)) or ((x in a) or (x in p))
        if f == False:
            break
    else:
        print(start, end, len(a))

# 53
