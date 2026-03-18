with open('26.6_13394.txt') as file:
    m = [int(x) for x in file.readlines()[1:]]

all = sum(m)
m = [x for x in m if x > 350]

m = sorted(m)[::-1]
# print(m)
# print(len(m) % 3)
sale_good = sum(int(x * 0.75) for x in m[2::3])

tri = len(m) // 3
sale_bad = sum(x * 0.75 for x in m[tri*2:tri*3])

print(all - sale_good, all - int(sale_bad))
# 3924309 4275729
# добра тем, кто составляет такие задачи (нет)

