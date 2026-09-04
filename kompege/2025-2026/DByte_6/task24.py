with open('24_20347.txt') as file:
    s = file.readline()

# print(set(s), len(s))
# print(len(s)/6**4)
# print(s.count('UPIT'))
ss = s
s = s.replace('UPIT', ' UPIT')
s = s.split()
# print(s[:3])
res = []
for i in range(len(s)-80):
    t = ''.join(s[i:i+81])[1:] + 'UPI'
    res.append([len(t), i, t])

m = max(res)
print(m)
print(m[2] in ss, m[2].count('UPIT'))

# 133274
