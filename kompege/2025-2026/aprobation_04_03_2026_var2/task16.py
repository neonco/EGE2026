print(2023*2022)

from functools import cache

@cache
def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

for i in range(1, 2000):
    f(i)

res = (f(2024) - 2*f(2023)) // f(2022)
print(res)

# 4090506