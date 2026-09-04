def f(x, end):
    if x == end:
        return 1
    if x < end:
        return 0
    left = x // 10
    right = x % 10
    if left > right:
        return f(x - 2, end) + f(right*10 + left, end)
    else:
        return f(x - 2, end)

print(f(49, 12))




# 41 -> 14
# 76 -> 67
# 67 -> no


# 1 2 3 4 5 6 7 8 9 10 11 12 13
# | |                   +1
# |   |                 +2