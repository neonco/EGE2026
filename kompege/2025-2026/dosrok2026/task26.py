from collections import Counter

with open('26_17643.txt') as f:
    m = [tuple(int(x) for x in s.split()) for s in f.readlines()[1:]]

prices = [price for id, price, cat in m]
sr = sum(prices) / len(prices)
print(sr)
high_price = [x for x in m if x[1] > sr]
low_price = [x for x in m if x[1] <= sr]

c = Counter(high_price)
print(c)
# (51786, 856, 0): 51, (46481, 856, 0): 51
print(c[(51786, 856, 1)])
print(c[(46481, 856, 1)])

print(856*51, 36)
# 43656 36
