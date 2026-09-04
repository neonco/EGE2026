# максимум при пяти B эквивалентен минимуму при семи B за вычетом двух лишних

with open('24_25335.txt') as file:
    s = file.readline()

print(set(s), len(s))
# для удобства добавляю фиктивные B-эшки слева и справа строки
# обязательно удалите последний \n
s = 'B' + s[:-1] + 'B'

ind = [i for i, bukva in enumerate(s) if bukva == 'B']

res = []
for x, y in zip(ind, ind[6:]):
    d = (y - x + 1) - 2
    res.append([d, x, y])

print(max(res))

# BAABBBAABAABAAAABAAAB
# 0  345  8  11   16  20