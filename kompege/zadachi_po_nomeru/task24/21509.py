with open('24_21509.txt') as file:
    s = file.readline()



s = s.replace('*', '-')
s = s.replace('-', '+')
for sym in '123456789':
    s = s.replace(sym, '1')
while '++' in s:
    s = s.replace('++', '  ')
s = s.replace(' +', '  ')
# s = s[:300]
s = s.split()

s = [x.split('+') for x in s]
s = [['0A1'+y[2:] if y[:2] == '01' else y for y in x] for x in s]
s = ['+'.join(x) for x in s]
s = 'A'.join(s)
s = s.split('A')

res = max(s, key=len)
print(res)
print(eval(res))
print(len(res))


