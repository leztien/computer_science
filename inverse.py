
"""MCA algorithm for matrix inverse"""


import random


def hash_matrix(matrix, return_tuple=False):
    t = tuple(sum(matrix, []))
    return t if return_tuple else hash(t)


def cache(func):
    d = dict()
    def closure(mx):
        key = hash_matrix(mx, return_tuple=True)
        result = d.get(key, None)
        if result is None:
            result = d.setdefault(key, func(mx))
        return result
    return closure


def make_matrix(n):
    return [[random.randint(-10,10) for j in range(n)] for i in range(n)]


def select_row(A):
    counts = [sum(bool(a) for a in row) for row in A]
    
    if not counts:
        print(A)
    
    mn = min(counts)
    for i in range(len(A)):
        if counts[i] == mn:
            return i


def submatrix(A,i,j):
    n = len(A)
    return [[A[i_][j_] for j_ in range(n) if j_ != j] for i_ in range(n) if i_ != i]


@cache
def det(A):
    n = len(A)
    # base case
    if n == 2:
        (a,b),(c,d) = A[0], A[1]
        return a*d - c*b
    # recursive case
    i = select_row(A)
    Summe = 0 # sum
    for j in range(n):
        if A[i][j] == 0:
            continue
        Summe += (-1)**(i+j) * A[i][j] * det(submatrix(A,i,j))
    return Summe



def minors(A):
    n = len(A)
    return [[det(submatrix(A,i,j)) 
             for j in range(n)] 
                for i in range(n)]

def hadamard_product(A, B):
    n = len(A)
    return [[A[i][j] * B[i][j] for j in range(n)] for i in range(n)]


def sign_grid(n):
    return [[(-1)**(i+j) for j in range(n)] for i in range(n)]


def cofactors(minors_matrix):
    n = len(minors_matrix)
    M, G = minors_matrix, sign_grid(n)
    return hadamard_product(M, G)


def transpose(A):
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]


def inverse(A):
    """MCA algorithm"""
    n = len(A)
    d = det(A)
    if d == 0:
        print("degenerate matrix")
        return None
    det_inv = 1.0 / d
    
    # case for 2x2-matrix
    if len(A) == 2:
        [a,b], [c,d] = A
        return [[d * det_inv, -b * det_inv], [-c * det_inv, a * det_inv]]
    
    # general case
    T = transpose(cofactors(minors(A)))
    return [[T[i][j] * det_inv for j in range(n)] for i in range(n)]



def dot(a,b):
    return sum(a*b for a,b in zip(a,b))


def matmul(A, B):
    m,n = len(A), len(B[0])
    T = transpose(B)
    return [[dot(A[i], T[j]) for j in range(n)] for i in range(m)]
    


##############################################################
## DEMO ##
if __name__ == '__main__':
    n = random.randint(2,10)
    A = make_matrix(n)
    
    print(*A, sep='\n')
    
    d = det(A)
    print("Determinant =", d, "\n")
    
    
    import numpy as np
    A_1 = inverse(A)
    print("inverse:\n", np.array(A_1).round(2))
    
    I = matmul(A, A_1)
    
    
    nd = np.array(I)
    print("\n\n", nd.round(5))
    print("\ntest passed:", (np.eye(len(A)) == nd.round(5)).all())
