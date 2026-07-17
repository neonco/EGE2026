from functools import cache

@cache
def f(n):
    if n < 220:
        return n
    return (n - 3) * f(n - 4)

for i in range(0, 124000):
    f(i)
    print(i)


res = (f(123817) - f(123813)) // (9 * f(123809))
print(res)

# 1703254170