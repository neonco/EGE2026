dels = []
for n in range(3, 1_000_000, 2):
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            break
    else:
        if str(n).count('3') == 2:
            dels.append(n)


# print(len(dels), dels)

print(3003**2)
for n in range(8_996_453, 8_996_453 + 100_000):
    for d in dels:
        if n % d == 0 and n//d in dels:
            print(n, d, n//d, d * n//d)
            break

# 9001609 24133
# 9002887 38639
# 9006149 38653
# 9012167 3853
# 9012373 23531



