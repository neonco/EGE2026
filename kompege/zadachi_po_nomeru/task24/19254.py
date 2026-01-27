with open('24_19254.txt') as f:
    s = f.readline()[:-1]

print(set(s))


s = s.replace('FSRQ', ' FSRQ')
s = s.split()
print(s[:30])
m = [len(x) for x in s]
print(m[:30])
res = [sum(m[i:i+81])+3-1 for i in range(len(m))]
print(max(res))

# 2379
