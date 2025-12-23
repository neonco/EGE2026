# Определите в прилагаемом файле максимальное количество идущих подряд символов,
# среди которых подстрока 2025 встречается не менее 90 раз
# и при этом содержится ровно 80 букв Y.

with open('24_23762.txt') as file:
    s = file.readline()

s = s.replace('Y', ' Y')
s = s.split()

m = []
for i in range(len(s)):
    m.append(''.join(s[i:i+81])[1:])

m = [s for s in m if s.count('2025') >= 90]
print(len(m))
m = [s for s in m if s.count('Y') == 80]
m = [len(s) for s in m]
print(max(m))



