for n in range(700_001, 700_010):
    for d in range(17, n, 10):
        if n % d == 0:
            print(n, d)
            break

# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167