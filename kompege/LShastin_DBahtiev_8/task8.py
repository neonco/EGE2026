from itertools import product

a = 'АГЕИМНРЯ'
res = 0
for i, word in enumerate(product(a, repeat=6)):
    if (i+1) % 2 == 0:
        if word[0] != 'Г':
            if word.count('И') >= 2:
                print(i + 1, word)
                res += 1

print(res)

# 25165
