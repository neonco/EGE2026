# считать строку
with open('24.txt') as f:
    s = f.readline()[:-1] # убираю \n (перенос строки)

# print(set(s))
for symbol in 'AEU':
    s = s.replace(symbol, 'A')

for symbol in 'BCDF':
    s = s.replace(symbol, 'B')

s = s.replace('BAB', 'XXX')
for symbol in 'AB':
    s = s.replace(symbol, ' ')

s = s.split()
print(len(max(s, key=len)) // 3) # можно, но не нужно

s = [len(x) // 3 for x in s]
# вместо строк оставляю их длину
# и делю на три (спрашивают про тройки символов)

print(max(s))
# print(s[:50])

# 6
