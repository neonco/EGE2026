def f(heap1, heap2, t, h=0):
    flag = h%2 == t%2
    if heap1 + heap2 >= 207:
        return flag
    if h > t:
        return False
    m = [
        f(heap1+1, heap2, t, h+1),
        f(heap1, heap2+1, t, h+1),
        f(heap1*2, heap2, t, h+1),
        f(heap1, heap2*2, t, h+1),
    ]
    return all(m) if flag else any(m)


for s in range(1, 189+1):
    for t in range(7):
        if f(17, s, t):
            print(s, t)
            break

