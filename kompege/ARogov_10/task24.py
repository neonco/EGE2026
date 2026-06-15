with open('24.txt') as f:
    s = f.readline()

print(set(s))
for sym in '13579':
    s = s.replace(sym, ' 1')

s = [x for x in s.split() if x.count('Q') >= 35]
for _ in range(1000):
    s = [x if x.count('Q') == 35 else x[:-1] for x in s]

s = [len(x) for x in s]
print(max(s))

# 317