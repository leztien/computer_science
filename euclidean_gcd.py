def decorator(func):
    """Handles negative input values as well as zeros"""
    def closure(*args, **kwargs):
        if any(arg == 0 for arg in args):
            return None
        args = tuple(abs(arg) for arg in args)
        return func(*args, **kwargs)
    return closure



@decorator
def gcd(a,b):
    """Naive GCD calculator"""
    # Swap values so that a >= b
    a,b = (a,b) if a >= b else (b,a)
    
    # Decreace the test value by 1 each loop
    for i in range(b, 0, -1):
        if b % i != 0: continue
        if a % i == 0:
            return i


@decorator
def gcd_euclidean(a,b):
    """Euclidiean algorithm for GCD"""
    while (a != b):
        a,b = (a,b) if (a >= b) else (b,a)   # makes sure a >= b
        c = a - b
        a,b = b,c
    return a



import random

def test(n_loops):
    for _ in range(n_loops):
        a,b = (random.randint(-100, 100) for _ in range(2))
    
        d1 = gcd(a,b)
        d2 = gcd_euclidean(a,b)
        print("{:>3} and {:>3} have the GCD = {:>3}".format(a, b, d1 if d1 is not None else str(d1)))
        assert d1==d2


def main():
    test(500)

if __name__ == '__main__': main()
