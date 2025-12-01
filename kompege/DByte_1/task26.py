with open('26_23977.txt') as file:
    m = file.readlines()

n = int(m[0])
m = m[2:]
m = [x.split() for x in m]
m = [[int(a), int(b)] for a, b in m]
m = sorted(m)

count = 0
ind = 0
mfc = [-1]*n

for start, end in m:
    for i in range(len(mfc)):
        if mfc[i] < start:
            mfc[i] = end
            count += 1
            ind = i + 1
            # print(start, end)
            break

print(count, ind)







# m = [
#     [1, 3, 5],
#     [1, 2, 6],
#     [0, -2, 1],
#     [0, -2, -1],
# ]
# print(sorted(m))