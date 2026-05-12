from collections import Counter
from pprint import pprint

with open('24_27777.txt') as file:
    s = file.readline().strip()

pprint(Counter(s))

cur = 0
res = 0

# 123XXX1234AXX
# 123000123450

for symbol in s:
    if symbol in '0123456789AB':
        cur += 1
        res = max(res, cur)
    else:
        cur = 0

print(res)

