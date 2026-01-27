with open('24_24895.txt') as f:
    s = f.readline()[:-1]

print(set(s))
test = s[:25]
# print(test)
# 693+4856145+92298386+364*

# нельзя чтоб 2 арифм. знака шли подряд, но между * и + разницы нет
s = s.replace('*', '+')
s = s.replace('++', '  ')
s = s.split()
s = [x for x in s if x.count('+') >= 39]

res = 0
for x in s:
    for start in range(0, len(x)):
        for end in range(start + 79, len(x)):
            t = x[start: end+1]
            if t.count('+') == 39:
                res = max(len(t), res)
            if t.count('+') > 39:
                break
print(res)


