import re

with open('24_17685.txt') as f:
    s = f.readline()

mask = r'(?:(?:[0]|[1-9][0-9]{0,})[+*]){1,}(?:[0]|[1-9][0-9]{0,})'
res = re.findall(mask, s)
res = [x for x in res if eval(x) == 0]
print(max(res, key=len))

# 144