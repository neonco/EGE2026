n = 2*2187**567 + 729**566 - 2*243**565 + 81**564 - 2*27**563 - 6561
print(n)

def f(n):
    res = 0
    while n > 0:
        if n % 27 > 9:
            res = res + 1
        n = n // 27
    return res

print(f(n))

# 940