with open('24_26549.txt') as file:
    s = file.readline()

# print(set(s))

s = s.replace('2025', '2025 ')
s = s.split()

res = 0
for i in range(len(s)):
    w = s[i-1][-3:]+''.join(s[i:i+50])
    if w.count('Y') >= 140:
        # print(w, w.count('2025'), w.count('Y'))
        res = max(res, len(w))

print(res)

# 938
