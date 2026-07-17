from functools import cache

@cache
def g(n):
    if n < 25:
        return n
    return (n-5) * g(n-6)

for i in range(0, 65000):
    g(i)

res = (g(60000) - 315 * g(59994)) / g(59988)
print(res)

# 3580143520