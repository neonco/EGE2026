def f(n):
    if n >= 1:
        return g(n-2) + 5

def g(n):
    if n < 8:
        return n + 3
    else:
        return g(n-1) + 2
    
print(f(100))