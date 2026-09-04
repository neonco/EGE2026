from fnmatch import fnmatch

for n in range(0, 10**8, 271):
    if fnmatch(str(n), '12??15*6'):
        print(n, n // 271)

# 1202156 4436
# 12001506 44286
# 12131586 44766
# 12421556 45836
# 12711526 46906