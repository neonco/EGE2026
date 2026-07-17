from functools import cache

@cache
def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

for i in range(100, 2000):
    f(i)

res = (f(2024) - 5*f(2023)) / f(2022)
print(res)
print(2021**2 - 4)