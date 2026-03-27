with open('24.txt') as file:
    s = file.readline()

print(s[:20])
alph = '123456789ABCDEF'

for sym in set(s):
    if sym not in alph:
        s = s.replace(sym, ' ')

print(s[:20])

s = s.split()
print(s[:20])

def f(word):
    c = 0
    for sym in word:
        if sym in '89ABCDEF':
            c += 1
    return c >= 12

s = [x for x in s if f(x)]
print(s[:20])

# C1A9B8E59EDD98 ответ 14