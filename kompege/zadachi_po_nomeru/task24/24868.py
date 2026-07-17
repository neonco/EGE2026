with open('24_24868.txt') as f:
    s = f.readline()

from string import ascii_uppercase
from itertools import combinations



for pair in combinations(ascii_uppercase, r=2):
    temp = []
    for sym in s:
        if sym in pair:
            temp.append(sym)
        else:
            temp.append(" ")
    temp = "".join(temp)
    temp = temp.split()
    res = max(temp, key=len)
    print(pair, len(res), res)