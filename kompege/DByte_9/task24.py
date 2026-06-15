from string import ascii_uppercase

with open("24_29803.txt") as f:
    s = f.readline()

# print(set(s))

print(s[:30])
for c in ascii_uppercase:
    s = s.replace(c, ' ')
print(s[:30])

s = s.split()
print(max(s, key=len))

res = []
for x in s:
    m = 0
    tt = ''
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            temp = x[i:j]
            if len(set(temp)) == 3:
                if len(temp) > m:
                    m = len(temp)
                    tt = temp
    res.append([m, tt])

# for x, l in zip(s, res):
#     print(x, l)

print(max(res))

