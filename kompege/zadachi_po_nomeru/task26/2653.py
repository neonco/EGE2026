with open('26_2653.txt') as file:
    m = file.readlines()[1:]

m = [int(x) for x in m]
m = sorted(m)

m = [1,1,3,7]

t = [1] + [0] * sum(m)
for coin in m:
    for i in range(coin, coin*2):
        t[i] += t[i-coin]
    print(t)