with open('24360.txt') as file:
    m = file.readlines()

m = [[int(x) for x in s.split()] for s in m]
m = [sorted(s) for s in m]

m = [sum(s) for s in m if (sum([s.count(el)//2 for el in set(s)]) >= 3) ^ (min(s)**2 in s)]

print(min(m))

# очень плохая задача для плохих людей
# ответ 98