from string import ascii_uppercase

with open('24_28799.txt') as f:
    s = f.readline().strip()

for sym in ascii_uppercase:
    s = s.replace(sym, ' ')

s = s.split()
# s = '111111111111111111111111112222222222' # max sum 10
def f(s, limit=200):
    l = 0
    r = 0
    flag = True
    cur_sum = int()
    res = 0
    while flag:
        while cur_sum < limit and r <= len(s):
            flag = (r < len(s)-2)
            cur_sum += int(s[r])
            r += 1
        while cur_sum >= limit:
            cur_sum -= int(s[l])
            l += 1
        res = max(res, r-l)
    return res

res = 0
for st in s:
    res = max(res, f(st))

print(res)
