from re import finditer

with open('24_29354.txt') as file:
    s = file.readline()

s = s.replace('BC', '2')

pattern = r'(?:(2[^2]*){191}2)'

m = [x.group().replace('2', 'BC') for x in finditer(pattern, s)]
res = max(m, key=len)[1:-1]
print(res, res.count('BC'), len(res))

# 2221 ответ не сходится(((