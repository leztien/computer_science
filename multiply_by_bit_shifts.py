"""
multiply a number by bit shifting
"""

def decimal_to_binary(n):
    result = []
    while n:
        n,r = divmod(n, 2)
        result.append(r)
    return result[::-1]


def multiply(n, m):
    binary = decimal_to_binary(m)
    shifts = [i for i,j in enumerate(binary[::-1]) if j]
    return sum(n << i for i in shifts)



if __name__ == '__main__':
    #TEST
    from random import randint
    n, m = randint(1, 25), randint(1, 25)
    ans = multiply(n,m)
    print(ans, n*m)
