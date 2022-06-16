

"""
the sieve algorithm
(for finding primes)
"""


def sieve(n):
    primes = []
    numbers = list(range(2, n+1))
    p = 2
    
    while p*p <= n:
        for e in range(p, n+1, p):
            if e in numbers:
                numbers.remove(e)
        primes.append(p)
        p = numbers[0]
        
    return primes + numbers  # will be sorted

    
def is_prime(n):
    if n == 2 or n == 5:
        return True
    if n <= 1 or n % 2 == 0 or str(n).endswith('5'):
        return False

    for i in range(3, n, 2):  # check only odd numbers
        if n % i == 0:
            return False
    return True   
        



if __name__ == "__main__":
    from random import randint
    
    for _ in range(10_000):
        n = randint(3, 200)
        primes = sieve(n)
        
        print(primes, n); print()
        
        if any(not is_prime(e) for e in primes):
            raise Exception(f"a non-prime detected in {primes}")
        if primes != sorted(primes):
            raise Exception("list not sorted")
        if any(is_prime(e) for e in range(primes[-1]+1, n+1)):
            raise Exception("a prime was skipped")

