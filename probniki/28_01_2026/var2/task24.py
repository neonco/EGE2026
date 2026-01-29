from collections import Counter

with open('24_2.txt') as file:
    s = file.readline()

print(set(s))

t = []
for a, b, c in zip(s, s[1:], s[2:]):
    if a == b:
        t.append(c)

print(Counter(t))
# K