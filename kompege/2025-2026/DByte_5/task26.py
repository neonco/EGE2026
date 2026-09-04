with open('26_21512.txt') as file:
    n, m, k = [int(x) for x in file.readline().split()]
    d = [[0 for _ in range(k)] for _ in range(m)]
    for _ in range(n):
        row, column = [int(x)-1 for x in file.readline().split()]
        d[row][column] = 1


res_row, res_col = 0, 0
pattern = [0 for _ in range(k)]
for ind, row in enumerate(d):
    for i in range(k):
        pattern[i] += row[i]
    for j in range(k):
        if pattern[j:j+3] == [0, 0, 0]:
            res_row, res_col = ind + 1, j + 1
            break
    else:
        print(res_row, res_col)
        break



# 1804 4434

