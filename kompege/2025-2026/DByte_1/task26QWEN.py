with open('26_23977.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    requests = []
    for _ in range(n):
        a, b = map(int, f.readline().split())
        requests.append((a, b))

# Сортируем по времени начала, а при равенстве — по времени окончания (по возрастанию)
requests.sort(key=lambda x: (x[0], x[1]))

window_free = [-1] * k
served = 0
last_win = 0

for start, end in requests:
    for i in range(k):
        if window_free[i] < start:
            window_free[i] = end
            served += 1
            last_win = i + 1
            print(window_free)
            break

print(served, last_win)