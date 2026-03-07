with open('26-192.txt') as f:
    m = f.readlines()[1:]

m = [x.split() for x in m]
m = [[int(id), int(size), color] for id, size, color in m]
r = [(size, id) for id, size, color in m if color == 'R']
g = [(size, id) for id, size, color in m if color == 'G']
b = [(size, id) for id, size, color in m if color == 'B']

r = sorted(r, key=lambda x: -x[0])
g = sorted(g, key=lambda x: -x[0])
b = sorted(b, key=lambda x: -x[0])

res = []
for red in r:
    tower = [red]
    for i, green in enumerate(g):
        if red[0] - green[0] >= 2:
            tower += [green]
            g = g[i+1:]
            break
    for i, blue in enumerate(b):
        if tower[-1][0] - blue[0] >= 2:
            tower += [blue]
            b = b[i+1:]
            break
    res.append(tower)
    if len(r)*len(g)*len(b) == 0:
        break

print(len(res), res[-1])

# 3238 1055






