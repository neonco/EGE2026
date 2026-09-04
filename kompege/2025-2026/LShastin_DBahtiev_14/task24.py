with open('24_29922.txt') as file:
    s = file.readline()

# print(set(s))
# print(s.count('2026'))
# print(s.count('Z'))


res = []
s = s.replace('Z', ' Z').split()
for i in range(0, len(s)):
    t = ''.join(s[i:i+121])
    t = t[1:]
    # print(t)
    # print(t.count('Z'))
    if t.count('2026') >= 210:
        res.append(t)

print(len(max(res, key=len)))

# 8922
