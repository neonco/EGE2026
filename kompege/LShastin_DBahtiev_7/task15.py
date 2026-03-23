b = range(120, 210+1)

for a in range(1, 2000):
    for x in range(1, 2000):
        f = (x % a == 0) or ((x not in b) or ((x % 53 != 0) or ((x + a) <= 417)))
        if not f:
            break
    else:
        print(a)

# 258