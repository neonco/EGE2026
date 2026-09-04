from functools import cache

@cache
def f(n):
    if n == 1:
        return 1
    return (n+1) * f(n-1)

for i in range(1, 2500):
    f(i)

res = ((f(2025) // 2026) + f(2024)) // f(2023)

print(res)

# 4050