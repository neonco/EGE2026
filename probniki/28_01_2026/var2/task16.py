def f(n):
    if n == 1:
        return 1
    return 2 * g(n-1) + 5*n

def g(n):
    if n == 1:
        return 1
    return f(n - 1) + 2 * n

res = f(4) + g(4)

print(res)

# 89