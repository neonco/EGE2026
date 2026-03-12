with open('26_6759.txt') as f:
    m = [int(x) for x in f.readlines()[1:]]

trio = len(m) // 3
ost = len(m) % 3
print(trio, ost)
m = sorted(m)[::-1]
print(sum(m[3310:]))
# 22262050
print(sum(m)-sum(m[2::3]))
# 33246829