for n in range(500_001, 500_100):
    for d in range(13, n, 10):
        if n % d == 0:
            print(n, d)
            break

# 500002 53
# 500004 43
# 500006 13
# 500010 7143
# 500011 4673