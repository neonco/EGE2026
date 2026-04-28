from re import finditer

# s = '0 1 2 3 (((56+-+00(067-889)(7182-15)(3222+745))'
with open('24_28007.txt') as f:
    s = f.readline()

a = r'([1-9][0-9]{0,}[12346789]|[12346789])'
b = r'([1-9][0-9]{0,}[05]|[5])'
pattern = fr'(\({a}[+-]{b}\))+'


res = [x.group() for x in finditer(pattern, s)]
print(len(max(res, key=len)))

# 55

