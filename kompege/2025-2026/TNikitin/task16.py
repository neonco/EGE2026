from functools import cache

@cache
def f(n):
    if n in [1, 2]:
        return f'{n}'
    else:
        return f(n-1) + '3' + f(n-2)


res = f(50)
count = res.count('32323') * 2
res = res.replace('32323', '')
count += res.count('323')
print(count)

# 7778742047