from sys import setrecursionlimit

setrecursionlimit(300_000)
def f(n):
    if n < 10:
        return 3
    return (n+4) * f(n-5)

# res = f(257_487)/683 + 67*f(257_477)/f(257_472)

res = (257_487+4)*(257_482+4)*(257_477+4) // 683
res = res + 67 * (257_477+4)
print(res)

# переполнение

# 24994270044009