with open('24_26074.txt') as file:
    s = file.readline()

for digit in '02468':
    s = s.replace(digit, ' '+digit)

s = s.split()
s = [x for x in s if x.count('F') >= 76]

for _ in range(100):
    s = [x if x.count('F') == 76 else x[:-1] for x in s]

s = [(len(x), x.count('F')) for x in s if 'QQ' not in x]
print(s)

# 163