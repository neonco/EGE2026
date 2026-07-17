def q0(symbol, index):
    if symbol == -1:
        return q1(-1, index-1)

def q1(symbol, index):
    if symbol == -1:
        return
    if symbol == 1:
        return
    if symbol == 0:
        return q1(1, index-1)


s = [-1, -1, 0, 1, 0, 1, -1, -1]
last = 6
