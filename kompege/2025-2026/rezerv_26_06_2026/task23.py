def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    if '1' in str(x):
        x_new = int(str(x).replace('1', '3'))
        return f(x+1, end) + f(x_new, end)
    if '1' not in str(x):
        return f(x+1, end)

print(f(10, 84))

# 480





