# обязательно .py и .txt в одной папке
# считываем строки и переводим в числа
with open('17_23901.txt') as file:
    m = file.readlines()

m = [int(s) for s in m]

count = 0
res_sum = 0

for i in range(len(m)-1):
    if [m[i] % 80, m[i+1] % 80].count(17) == 1:
        if [m[i] % 7, m[i+1] % 7].count(0) == 2:
            # print(m[i], m[i+1])
            count += 1
            res_sum += sum([x for x in m[i:i+2] if x % 80 == 17])

print(count, res_sum)

# 48 2186016