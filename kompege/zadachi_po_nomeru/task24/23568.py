with open('24_23568.txt') as file:
    s = file.readline()

# print(set(s))

res = 0
ind = [i for i, x in enumerate(s) if x.isalpha()]
# print(len(ind))

for x, y in zip(ind, ind[1:]):
    if s[x] == s[y]:
        res = max(res, y-x+1)
        if res == 1952:
            print(x, y)
            break

# 310030
