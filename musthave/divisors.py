def f(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            res.append(d)
            res.append(n // d)
    return sorted(set(res))

