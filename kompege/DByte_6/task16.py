def f(n):
    if n == 0:
        return 0
    return n % 10 + f(n//10)

res = (2*f(13657) - f(13640)) / f(11000)

print(res)