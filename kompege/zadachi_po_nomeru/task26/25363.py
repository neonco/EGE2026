with open('26_25363.txt') as file:
    n = int(file.readline())
    data = file.readlines()

data = [[int(x) for x in el.split()] for el in data]
data = [x + [ind+1] for ind, x in enumerate(data)]
print(data[-1])

data_active = [x for x in data if x[1] > x[0]]
data_sleep = [x for x in data if x[0] > x[1]]
res = data_active + data_sleep[::-1]
print(len(data_sleep)-1)
print(res[0])
