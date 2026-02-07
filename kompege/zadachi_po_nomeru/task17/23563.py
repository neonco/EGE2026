with open('17_23563.txt') as file:
    m = [int(s) for s in file.readlines()]


# минимальный положительный элемент
# последовательности, кратный 35
limit = min([x for x in m if x > 0 and x % 35 == 0])
# 210

res = []
for a, b in zip(m, m[1:]):
    if a != b:
        if abs(a - b) % limit == 0:
            res.append(a+b)

print(len(res), max(res))