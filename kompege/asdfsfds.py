def square(a, b, c):
    p = (a + b + c) / 2
    res = p*(p-a)*(p-b)*(p-c)
    return res**0.5


for a in range(1, 1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            if c < a + b:
                s = square(a, b, c)
                if s % 1 == 0:
                    if s == a+b+c:
                        print(a, b, c, s)
