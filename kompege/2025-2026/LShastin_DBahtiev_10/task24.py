from collections import Counter
from pprint import pprint
import re

with open('24.txt') as file:
    s = file.readline()

pprint(Counter(s))
print(len(s))

t = r'(?:[13579]|[1-9][0-9]{0,7}[13579])'
mask = rf'(?:{t}[-*])*{t}'
res = [x.group() for x in re.finditer(mask, s)]
print(max(res, key=len))
print(len(max(res, key=len)))

# 81, но надо смотреть чтоб ни одно число не начиналось на 0



