def is_triange(a, b, c):
    big = max(a, b, c)
    sum_small = (a + b + c) - big
    return big < sum_small

for a in range(1, 1500):
    for x in range(1, 1500):
        f = (not is_triange(x, 10, 20) or not ((max(x, 8)) > 24)) == (not is_triange(3, a, x))
        if f == 0:
            break
    else:
        print(a)

# 27