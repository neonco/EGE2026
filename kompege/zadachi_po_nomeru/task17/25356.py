# Определите количество троек элементов
# последовательности, в которых ни один из трёх элементов
# не является четырёхзначным числом, а сумма элементов
# тройки больше максимального элемента последовательности,
# оканчивающегося на 30. В ответе запишите количество
# найденных троек чисел, затем максимальную из сумм
# элементов таких троек.

with open('17_25356.txt') as file:
    m = file.readlines()

m = [int(s) for s in m]

limit = max([x for x in m if str(x)[-2:] == '30'])
print(limit)

count = 0
max_sum = float('-inf')
for i in range(len(m)-2):
    a, b, c = m[i:i+3]
    if len(str(abs(a))) != 4 and len(str(abs(b))) != 4 and len(str(abs(c))) != 4:
        if a + b + c > limit:
            count += 1
            max_sum = max(max_sum, a + b + c)

print(count, max_sum)

res = []
for trio in zip(m, m[1:], m[2:]):
    cond = [x for x in trio if len(str(abs(x))) != 4]
    if len(cond) == 3:
        if sum(trio) > limit:
            res.append(sum(trio))

print(len(res), max(res))
# 1032 285423

