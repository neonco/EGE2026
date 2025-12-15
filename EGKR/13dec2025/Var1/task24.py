with open('24.txt') as file:
    s = file.readline()

for a in '02468':
    s = s.replace(a, '2')
s = s.replace('2', ' 2')
s = s.split()
s = [x for x in s if x.count('F') >= 76]

for x in s:
    print(x.count('F'), x)

for x in s:
    while x.count('F') > 76:
        x = x[:-1]
    print(x, x.count('F'), len(x))

# 163
