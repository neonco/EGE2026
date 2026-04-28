from re import finditer

with open('24_28943.txt') as f:
    s = f.readline()

s = s.replace('20', 'Ю')

pattern = r'((Ю[^ЮAEIOUY]*){26}[AEIOUY])'

m = [x.group().replace('Ю', '20') for x in finditer(pattern, s)]
res = min(m, key=len)
print(res, len(res))

# 58
