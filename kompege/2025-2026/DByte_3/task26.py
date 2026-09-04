with open('26_24870.txt') as f:
    data = f.readlines()

n, m = data[0].split()
n, m = int(n), int(m)
data = data[1:]
factories = data[:n]
generators = data[n:]

factories = [int(factory) for factory in factories]
# print(len(factories), len([x for x in factories if x <= 963])) чисто для интереса
generators = [[int(x) for x in gen.split()] for gen in generators]
generators = [[price, power] for power, price in generators]
generators = sorted(generators)
print(generators[:10])

res_sum_price = 0
res_max_power = 0
for i, factory in enumerate(factories):
    if i % 100 == 0:
        print(i)
    for price, power in generators:
        if power >= factory:
            res_sum_price += price
            res_max_power = max(res_max_power, power)
            break

print(res_sum_price, res_max_power)

# 100512346 1000

