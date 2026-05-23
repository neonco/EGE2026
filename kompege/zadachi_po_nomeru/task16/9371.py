from functools import cache

@cache
def f(n):
    if n >= 3210:
        return 1
    return f(n+3) + 7

@cache
def g(n):
    if n < 10:
        return n
    return g(n-3) + 5

for i in range(1, 5000):
    g(i)

for i in range(5000, 1, -1):
    f(i)

print(f(15))
print(g(3000))
print(f(15)-g(3000))