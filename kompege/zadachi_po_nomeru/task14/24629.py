from string import digits, ascii_uppercase

def f(n, base):
    res = ''
    alphabet = digits + ascii_uppercase
    while n > 0:
        res += alphabet[n % base]
        n //= base
    return res[::-1]

n = 14**1402 + 28**501 - 14**51 - 1400
print(f(n, 14).count('C'))

# 8