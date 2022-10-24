"""
euclidean algorithms (iterative vs recursive)
"""



from math import gcd
from random import randint


def generate():
    a,b = sorted((randint(2,100) for _ in range(2)), reverse=True)
    if randint(0,1): return a,b
    d = randint(1,50)
    m,n = (randint(2,15) for _ in range(2))
    a,b = sorted((d*k for k in (m,n)), reverse=True)
    return a,b



a,b = generate()


def gcd_iterative(a,b):
    while a != b:
        c = a - b
        a,b = (b,c) if b>c else (c,b)    
    return a


d = gcd_iterative(a, b)
print(d)



def gcd_recursive(a,b):
    m,r = divmod(a,b)
    # base case
    if r == 0:
        return b
    # recursive case
    return gcd_recursive(b, r)

d = gcd_recursive(a, b)
print(d)

d = gcd(a,b)
print(f"gcd({a},{b}) = {d}")
