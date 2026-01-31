from string import digits, ascii_uppercase

def dec_to_12(n):
    res = ''
    a = digits + ascii_uppercase
    while n > 0:
        res = a[n % 12] + res
        n = n // 12
    return res


for n in range(1, 1000):
    n12 = dec_to_12(n) # 1
    # print(n12)

    if n % 3 == 0:
        n12 = 'B' + n12 + '2' # 2а
    else:
        n12 = '1' + n12 + '0'  #2b
    # print(n12)

    r = int(n12, base=12) # 3
    if 2500 < r < 2510:
        print(n, r)

# 2508
