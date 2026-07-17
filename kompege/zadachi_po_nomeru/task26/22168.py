with open('26_22168.txt') as file:
    n = int(file.readline())
    data = file.readlines()

d = dict()
for pair in data:
    student, task = [int(x) for x in pair.split()]
    if task % 2 == 0:
        if student in d.keys():
            d[student].add(task)
        else:
            d[student] = {task}

res = [[len(tasks), -stud] for stud, tasks in d.items()]
res = sorted(res)
print(res[-20:])

# 271802 21






