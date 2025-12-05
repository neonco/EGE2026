# из произвольной в десятичную (до основания 36)

x = 'ABC456M'
print(int(x, base=30))
# 7567132702


# из десятичной в произвольную (основания от 2 до 36)
from string import digits, ascii_uppercase

def dec_to_base(n, base=10):
    res = ''
    alph = digits + ascii_uppercase # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    while n > 0:
        res += alph[n % base]
        n //= base
    return res[::-1]

print(dec_to_base(123, base=12)) # A3


# из произвольной в десятичную (от основания 2 до много-много)

from string import digits, ascii_uppercase

def base_to_dec_all(x, base=10):
    alph = digits + ascii_uppercase
    x = [alph.index(symbol) for symbol in x]
    res = 0
    for i, digit in enumerate(x[::-1]):
        res += digit * base ** i
    return res

print(base_to_dec_all('ABCD123', base=123))
# 34940714388504



