n = 13**1402 + 11**501 - 12**51 - 2323

count = 0
while n > 0:
    if 9 < n % 27 <= 20:
        count += 1
    n //= 27

print(count)