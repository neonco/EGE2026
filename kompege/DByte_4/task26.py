with open('26_25337.txt') as f:
    n = int(f.readline())
    d = [[0 for _ in range(1441)] for _ in range(n)]
    for row in d:
        start, end = [int(x) for x in f.readline().split()]
        for i in range(start, end+1):
            row[i] = 1

pattern = [0 for _ in range(1441)]
for row in d:
    for i, cell in enumerate(row):
        pattern[i] += cell

res_max = max(pattern)
res = ['A' if x == res_max else ' ' for x in pattern]
res = ''.join(res).split()
res_period = len(res)
print(res_period, res_max)
# 2 232



