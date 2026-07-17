for n in range(1, 70):

    b = bin(n)[2:]

    s = sum([int(x) for x in b])
    b = b + str(s % 2)

    s = sum([int(x) for x in b])
    b = b + str(s % 2)

    r = int(b, base=2)
    print(n, r)

# 64 258