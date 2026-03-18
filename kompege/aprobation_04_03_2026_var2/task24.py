with open('24_27777.txt') as f:
    s = f.readline()[:-1]

new_s = []
for sym in s:
    if sym == '0':
        new_s.append(sym)
    elif sym in '123456789AB':
        new_s.append('1')
    else:
        new_s.append(' ')

s = ''.join(new_s).split()
s = [len(x.lstrip('0')) for x in s]
print(max(s))

# 18