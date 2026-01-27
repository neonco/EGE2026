def f(n):
    if n >= 67:
        return n
    else:
        return 3 * (g(n-2) - 1)

def g(n):
    if n >= 52_000:
        return n / 10 + 30
    return g(n+1) - 1/2

print(f(10007))

# 10007 - задача с приколом