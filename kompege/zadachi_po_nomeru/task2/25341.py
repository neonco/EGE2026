for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (w == z) or not(not y or w) or not x
                if f == 0:
                    print(z, w, x, y, f)

# zwxy

# y   w   y -> w   y <= w  not y or w
# 0   0      1        1         1
# 0   1      1        1         1
# 1   0      0        0         0
# 1   1      1        1         1


# print(int(True))
# print(int(False))
# print(bool(1))
# print(bool(0))
# print(bool(-123))
# print(bool(1111111111))
#
# print(0 or -21323232 or 1 or 3)
# print(False or True)








