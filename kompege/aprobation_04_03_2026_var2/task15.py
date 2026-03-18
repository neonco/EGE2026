for a in range(1, 1500):
    for x in range(1, 1500):
        f = (x % 21 != 0) or ((x % a == 0) or (x % 77 != 0))
        if f == False:
            break
    else:
        print(a)

# 231