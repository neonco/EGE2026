t = [
    [[' ',-1,1], ['0',-1,1], ['1', 1,0]],
    [[' ',-1,2], ['1', 1,3], ['0',-1,3]],
    [[' ',-1,2], ['1',-1,2], ['1', 1,0]],
    [[' ', 0,2], ['0',-1,3], ['1',-1,1]],
]

s = ' '*1000 + '0'*250 + '1'*500 + '0'*250 + ' '
s = list(s)
def f(sym=' ', i=-1, row=0):
    col = ' 01'.index(sym)
    state = i
    sym, move, row = t[row][col]
    if i == 0:
        return ''.join(s)
    s[state + move] = sym
    f(sym, state, row)

s = list(' 00 ')
print(f())