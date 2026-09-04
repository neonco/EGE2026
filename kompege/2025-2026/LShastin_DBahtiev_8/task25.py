from fnmatch import fnmatch

def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res += [d, n//d]
    return sorted(set(res))

for n in range(0, 10**9, 3117):
    if fnmatch(str(n), '571*9?'):
        t = [x for x in f(n) if x % 2]
        if sum(t) % 8 == 0:
            print(n, sum(t))

# 5719695 9185280
# 57112791 77575680
# 57131493 76252800
# 57150195 96844800
# 57168897 76302720
# 57187599 87260160
# 571015698 419386240