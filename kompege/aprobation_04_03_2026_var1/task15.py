for a in range(1, 2000):
    for x in range(1, 2000):
        f = (x % 25 != 0) or ((x % a == 0) or (x % 60 != 0))
        if not f:
            break
    else:
        print(a)