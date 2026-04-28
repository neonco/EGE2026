import re

with open('24_28006.txt') as f:
    s = f.readline()

a = r'([1-9][0-9]*[02468]|[2468])'
b = r'([1-9][0-9]*[13579]|[13579])'
pattern = rf'(\({a}[-+]{b}\))+'


m = [x.group() for x in re.finditer(pattern, s)]
res = max(m, key=len)
print(len(res))

# 89