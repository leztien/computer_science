"""
Euclidean algorithm computing the 
Greatest Common Divisor of two integers

as well as the
Least Common Multiple
"""


def euclidean_algorithm(a, b):
    while a != b:
        if b > a:
            a,b = b,a
        a = a - b
    return a


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)
