m = range(32, 68+1)
n = range(54, 76+1)

pairs = []
for first in range(-100, 300):
    for second in range(first+1, 300):
        pairs.append([first, second])

# перебор параметра А
for start, end in pairs:
    a = range(start, end+1)
    # перебираю переменные
    for x in range(-100, 400):
        f = not((x in m) or (x in n)) == (x not in a)
        if f == 0:
            break
    else:
        print(a, start, end, end-start)

# 44





