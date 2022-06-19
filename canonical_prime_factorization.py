
"""
Kanonische Primfaktorenzerlegung (canonical prime factorization)
(the tree method from the book by Weitz)
"""


from operator import mul
from functools import reduce
from random import randint



def is_prime(n):
    if n == 2 or n == 5:
        return True
    if n <= 1 or n % 2 == 0 or str(n).endswith('5'):
        return False

    for i in range(3, n, 2):  # check only odd numbers
        if n % i == 0:
            return False
    return True



def kanonische_primfaktorenzerlegung(n):
    if n <= 1:
        return None
    
    factors = []
        
    def recursive(n):
        # Base Case
        if is_prime(n):
            factors.append(n)
            return
        
        # Recursive Case
        f = int(n ** (1/2))
        while True:
            if n % f == 0:
                break
            else:
                f -= 1
                continue
        # recurse from here
        recursive(f)
        recursive(n // f)
    
    # Start recursion
    recursive(n)
    return sorted(factors)
    


def check_result(list, n = None):
    if sum(not is_prime(n) for n in list) > 0:
        raise Exception("non-prime detected")
    result = reduce(mul, list)
    return result == n if n else result




# Demo
if __name__ == "__main__":
    n = 4200
    factors = kanonische_primfaktorenzerlegung(n)
    print(factors, check_result(factors))

    # multiple tests
    mx = randint(100, 5000)
    for _ in range(mx * 2):
        n = randint(2, mx)
        factors = kanonische_primfaktorenzerlegung(n)
        
        b = check_result(factors, n)
        if not b:
            raise ValueError(f"n = {n}, bad factors = {factors}")
        print(n, factors, b)

