"""
The 'compute_next_permutation' function is the code which I found at
https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

However I internalized that algorithm and completely rewrote the function
"""


def compute_next_permutation(seq):
    """
    Computes the next permutation algorithmically
    in contrast to creating all permutations recursivelly which would take O(N!)
    """
    # we need a list because of some in-place swapping later in the code
    a = list(seq)
    
    # find the longest monatonically decreasing suffix / tail
    suffix_start = 0
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            suffix_start = i+1
    # if the whole array is already monatonically decreasing 
    # i.e. it is in descending order
    # then it is already the largest permutation - return None
    if suffix_start == 0:
        return None
    
    # identify the pivot (the cell to the left of the suffix)
    pivot = suffix_start - 1
    
    # identify the smallest in the suffix, 
    # but which is bigger than the pivot value
    i = len(a) - 1
    while a[pivot] >= a[i]:
        i -= 1
        
    # swap the pivot and the "anti-pivot"
    a[pivot], a[i] = a[i], a[pivot]
    
    # reverse the suffix
    a[pivot+1 :] = a[pivot+1 :][::-1]
    return tuple(a)
        

def next_bigger(n):
    """wrapper function for the 'compute_next_permutation' function"""
    # split n into digits and send the sequence of digits into the compute_next_permutation function
    seq = compute_next_permutation([int(e) for e in str(n)])
    
    # if n is the largest pemutation already
    if seq is None:
        return -1
    
    # assemble the sequence of digits into an intiger
    return int(''.join(str(e) for e in seq))






"""
My fisrt attempt that worked but didn't pass because of time limit 
due to the algorithm's inefficiency:
"""

from functools import lru_cache
from itertools import permutations

@lru_cache(maxsize=128)
def get_permutations(n):
    return tuple(permutations(range(n), r=n))


def encode_number(n):
    mapping = {k:int(v) for k,v in enumerate(sorted(str(n)))}
    pairs = sorted(pair[::-1] for pair in mapping.items())
    
    encoded_number = []
    
    for digit in str(n):
        for ix in range(len(pairs)):
            if int(digit) == pairs[ix][0]:
                encoded_number.append(pairs[ix][1])
                del pairs[ix]
                break
    return tuple(encoded_number)
            

def next_bigger_inefficient(n):
    mapping = {k:v for k,v in enumerate(sorted(str(n)))}

    encoded = encode_number(n)
    
    perms = get_permutations(len(str(n)))
    
    ix = perms.index(encoded)
    
    if ix == len(perms)-1:
        return -1
    
    for perm in perms[ix+1:]:
        candidate = int(''.join(mapping[k] for k in perm))
        if candidate > n:
            return candidate
    return -1



### TEST ###
if __name__ == '__main__':
    
    
    perm = "AABCC"
    while perm:
        perm = compute_next_permutation(perm)
        print(perm)
    
    
