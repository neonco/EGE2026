with open('24_28943.txt') as f:
    s = f.readline()

for sym in 'AEIOUY':
    s = s.replace(sym, 'A')

s = s.replace('20', '2 0')
s = s.split()

res = []
for i in range(len(s)-25):
    cur = ''.join(s[i:i+25])
    cur = '2' + cur
    dob = s[i+25]
    if cur.count('A') == 0 and 'A' in dob:
        j = dob.find('A')
        cur = cur + dob[:j+1]
        res.append(len(cur))
        # print(len(cur), cur, dob, j,  cur.count('20'), cur.count('A'))

print(min(res))

# 58

