with open('24_24977.txt') as f:
    s = f.readline()

# 2?0?2?6

cnt = 0
l = 0
res = 0
for r in range(6, len(s)):
    if s[r-6]+s[r-4]+s[r-2]+s[r] == '2026':
        cnt += 1
    while cnt > 10:
        if s[l]+s[l+2]+s[l+4]+s[l+6] == '2026':
            cnt -= 1
        l += 1
    res = max(res, r - l + 1)
print(res)

# 942





