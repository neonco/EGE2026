with open('26_28801.txt') as f:
    n, k = [int(x) for x in f.readline().split()]
    m = [[int(x) for x in s.split()] for s in f.readlines()]

m = [[*x, x[0]+x[3], 0] for x in m]
m = sorted(m, key=lambda x: (x[0], -x[2], x[3], x[1]))
ch = [0]*10
print(ch)

res1 = 0
for t in range(0, 1440):
    q = [[i, *x] for i, x in enumerate(m) if x[0] <= t and x[4] >= t and x[5]==0]
    for i in range(len(q)):
        ind, ar, cht, pr, bt, dead, chid = q[i]
        for j in range(len(ch)):
            if ar >= ch[j]:
                ch[j] = ar+cht
                m[ind][5] = j+1
                q[i][6] = j+1
                res1 += 1
                break

print(res1, m[-10:])
#
# ответы минимально отличаются от авторских, возможна ошибка автора
#
#
#
# with open("26_28801.txt") as file:
#     total_robots, total_chargers = map(int, file.readline().split())
#     # [arrival, charge_time, priority, battery_time]
#     data = []
#     for i in file.readlines():
#         data.append(list(map(int, i.split())))
# data = sorted(data, key=lambda x: x[0])
# chargers = [[i, 0] for i in range(1, total_chargers + 1)]
# queue = []
# count = 0
# for minute in range(1500):
#     queue.extend([i for i in data if i[0] == minute])
#     chargers = [i if i[1] > minute else [i[0], 0] for i in chargers]
#     while not all([i[1] for i in chargers]):
#         if len(queue):
#             candidate = sorted(queue, key=lambda x: (1000 - x[2], x[0] + x[3] - minute, x[1]))[0]
#             queue.remove(candidate)
#             sorted([i for i in chargers if i[1] == 0], key=lambda x: x[0])[0][1] = minute + candidate[1]
#             count += 1
#         else:
#             break
#     queue = [i for i in queue if i[0] + i[3] < minute]
#     print(minute, queue, chargers)
# print(count)
