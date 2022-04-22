"""
naive function that determines whether a number is prime
"""

def is_prime(n):
    if n == 2 or n == 5:
        return True
    if n <= 1 or n % 2 == 0 or str(n).endswith('5'):
        print("\nFALSE")
        return False

    for i in range(3, n, 2):  # check only odd numbers
        if n % i == 0:
            return False
    return True
