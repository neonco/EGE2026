from itertools import product

alph = 'МАНГУСТ'

res = 0
for var in product(alph, repeat=6):
    word = ''.join(var)
    if word[0] != 'А':
        if word.count('У') > 0:
            if word.count('М') == 2:
                # print(word) 
                res += 1

print(res)
# 9155
