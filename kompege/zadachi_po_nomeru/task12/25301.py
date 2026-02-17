t = [
    [[' ', -1, 0], ['1', 0, 1 ], ['0', -1, 1]],
    [['1', 0, 1 ], ['1', 0, 0 ], ['0', -1, 1]],
]

s = ' '*2 + '0'*343 + '1'*656 + '0' + ' '*2
s = list(s)

sym, move, state = [' ', -1, 0]
print(s)

i = 1002
while move != 0:
    sym = s[i]
    cell = t[state][' 01'.index(sym)]
    s[i] = cell[0]
    move = cell[1]
    i += move
    state = cell[2]

print(s.count('0'))

# 344