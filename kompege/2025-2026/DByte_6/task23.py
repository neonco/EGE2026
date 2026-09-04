def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    return f(x+1, end) + f(x+5, end) + f(x*5, end)


a = f(3, 10) * f(10, 25)
b = f(3, 20) * f(20, 25)
c = f(3, 10) * f(10, 20) * f(20, 25)
print(a, b, c)
print(a + b - c - c)

# 134