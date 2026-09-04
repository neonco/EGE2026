def f(n):
    if n < 15:
        return 4
    return (n + 7) * f(n - 6)

res = (f(1223) // 203 + f(1211) // 29) // f(1205)
print(res)