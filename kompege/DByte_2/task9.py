with open('task9.txt') as f:
    m = f.readlines()

m = [el.split() for el in m]
m = [[int(x) for x in string] for string in m]
# print(m)

for string in m:
    if len(set(string)) == len(string):
        even = [x for x in string if x % 2 == 0]
        if len(even) == 3:
            if min(string)*2 == sum(even) / 3:
                print(string)
# в ответ 42 как сумму первой выведенной строки
