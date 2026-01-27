import re

with open('24_25361.txt') as file:
    s = file.readline()

print(len(s))
pattern = r'(?=([02468](?:[^F02468]*F){76}[^F02468]*))'
pattern = re.compile(pattern)
res = re.findall(pattern, s)
for x in res:
    print(len(x), x)

# 163