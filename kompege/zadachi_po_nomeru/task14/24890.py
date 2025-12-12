from string import digits, ascii_uppercase

def f(n, base):
    res = ''
    alphabet = digits + ascii_uppercase
    while n > 0:
        res += alphabet[n % base]
        n //= base
    return res[::-1]


n = 27**298 + 27**269
for x in range(1, 7290+1):
    s = f(n-x, 27)
    print(x, s.count('0'))

# 31
