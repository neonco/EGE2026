with open('task24.txt') as f:
    s = f.readline()[:-1]

print(len(s), set(s))

#aaaaab caaaaab caaaab cb caaaaab caaaaa
#aaaaab caaaaab caaaab
#       caaaaab caaaab cb
#               caaaab cb caaaaab
#                      cb caaaaab caaaaa

s = s.replace('BC', 'B C')
s = s.split()
res = []
for i in range(len(s)):
    t = s[i:i+181]
    # print(len(t))
    t = ''.join(t)
    # print(t.count('BC'))
    res.append(len(t))

print(max(res))