
"""
Stellenwertsysteme - Umrechnung
"""

def binary_to_decimal(n: str):
    BASE = 2
    result = 0
    for i,digit in enumerate(n):
        result = (result + int(digit)) * (BASE if i < len(n)-1 else 1)
    return result


def decimal_to_binary_subtraction_method(n):
    """
    Converts a positive decimal number into binary
    """
    # Do not accept negative numbers of non-integeres
    if type(n) is not int or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # If the input is zero then return zero
    if n == 0:
        return '0'
    
    # Make a list of squared numbers
    seq = [1,]
    while seq[-1] <= n:
        seq.append(seq[-1] * 2)
    seq.pop()
    
    # The crux of the whole algorithm is this loop
    for i in range(len(seq)-1, -1, -1):
        r = n - seq[i]
        if r >= 0:
            seq[i] = 1
            n = r
        else:
            seq[i] = 0
    
    # Reverse the list and join it into a str
    seq.reverse()
    return str.join('', (str(e) for e in seq))


def decimal_to_binary_division_method(n):
    bits = []
    while n > 0:
        n,r = divmod(n, 2)
        bits.append(r)
    return ''.join(str(e) for e in bits[::-1]) or '0'
    

def decimal_to_hexadecimal(n):
    d = {i:str(i) for i in range(10)}; d.update({i:s for i,s in zip(range(10, 17), "ABCDEF")})
    bits = []
    while n:
        n,r = divmod(n, 16)
        bits.append(d[r])
    return ''.join(bits[::-1]) or '0'

