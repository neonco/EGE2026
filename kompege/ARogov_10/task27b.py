from pprint import pprint
from collections import Counter
from math import dist

with open('9. 27-Ð_.txt') as f:
    m = [[float(x) for x in s.replace(',','.').split()] for s in f.readlines()]

def f(point):
    x, y = point
    return (x*x+y*y <= 4, x <= 1, y <= x + 2, y <= -3, x <= 0, y <= 0)

t = [f(p) for p in m]
pprint(Counter(t))

pat1 = (False, True, True, False, True, True)
pat2 = (True, True, False, False, True, False)
pat3 = (True, False, True, False, False)

m1 = [p for p in m if f(p) == pat1]
m2 = [p for p in m if f(p) == pat2]
m3 = [p for p in m if f(p)[:-1] == pat3]
print(len(m1))
print(len(m2))
print(len(m3))