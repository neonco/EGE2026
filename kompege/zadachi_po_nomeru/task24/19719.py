from collections import Counter

with open('24.12_19719.txt') as file:
    s = file.readline()

print(Counter(s))

for sign in '-*':
    s = s.replace(sign, '@')
s = s.replace('@0', '@0 ')
s = s.replace('@@', '@ @')
s = s.split()
s = ['b' + x.lstrip('0') if x[0] == '0' and x != '0' else x for x in s]
print(s[:100])