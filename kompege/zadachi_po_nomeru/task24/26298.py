with open('24.txt') as f:
    s =  f.readline()

print(len(s), set(s))

# s = 'ABCCCCAXXXXXXXXXXXXXXXXZZZZ'
s = s + ' '
t = []
count = 1
for a, b in zip(s, s[1:]):
    if count == 5:
        t.append(f'{count}{a}')
        count = 1
    elif a != b:
        if count == 1:
            t.append(f'{a}')
            count = 1
        else:
            t.append(f'{count}{a}')
            count = 1
    else:
        count += 1

res = ''.join(t)
# print(s)
# print(res)
print((len(s)-1 - len(res)) * 8)

