p = range(5, 54+1)
q = range(50, 93+1)

for a in range(-100, 400):
    m = []
    for x in range(-100, 400):
        f = not((x not in p) and (x in q)) or (x > a)
        m.append(int(f))
    if m.count(0) == 20:
        print(a)

# 74






