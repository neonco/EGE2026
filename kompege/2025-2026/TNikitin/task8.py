from itertools import product

def f(word):
    res = ''
    for sym in word:
        if sym in 'ОЯИЕ':
            res += 'g'
        elif sym in 'ЪЬ':
            res += 'y'
        else:
            res += 's'
    return res

count = 0
alph = sorted('ОБЪЯВИТЕЛЬ')
k = 0
for x in product(alph, repeat=6):
    k += 1
    if k % 2 == 0:
        if x.count('О') <= 2:
            word = f(x)
            if 'gg' not in word:
                if word[0] != 's':
                    if word[-1] != 's':
                        count += 1
print(count)






