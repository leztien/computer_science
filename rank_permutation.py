
"""
rank a permutation (with or without repitition)
"""

from collections import Counter
from functools import reduce, lru_cache
from operator import mul


@lru_cache(maxsize=128)
def fact(n):
    if n <= 1: return 1
    return fact(n-1) * n


def rank(permutation):
    """
    Rank a non-repitition permutation (i.e. all elements must be unique).
    This algorithm is over ten times faster than 'rank_repetition'
    (only for permutations without repitition, of course)
    
    I derived this algorithm from the explanation at:
    https://www.dcode.fr/permutation-rank
    """
    
    # make the "alphabet" of the permutation
    abc = sorted(set(permutation))
    
    assert len(abc) == len(permutation), "no repition allowed!"
    
    # initialize the sum with 0
    s = 0
    
    # iterate over each character in the permutation
    for c in permutation:
        p = abc.index(c)
        s += p * fact(len(abc) - 1)
        abc.remove(c)
    return s


def rank_repetition(permutation):
    """
    Ranks a permutation with repitition.
    
    I derived this algorithm from the explanation in the comment section at
    https://praty23.wordpress.com/2012/05/15/rank-of-a-word-in-dictionary/
    """
    perm = list(permutation)
    s = 0
    
    while perm:
        for c in sorted(set(perm)):
            if c == perm[0]:
                perm = perm[1:]
                break
        
            k = Counter(perm)
            k.subtract({c})
            k = (k for k in k.values() if k > 1)
            s += fact(len(perm) - 1) // reduce(mul, map(fact, k), 1)
    return s
        

def rank_permutation(permutation):
    """
    A wrapper function for the 'rank' and 'rank_repitition' functions
    """
    if len(set(permutation)) == len(permutation):
        return rank(permutation)
    return rank_repetition(permutation)



    
# TEST
if __name__ == '__main__':
    
    ans = rank_repetition("ZYXWVUTSRQPONMLKJIHGFEDCBA")
    print(ans)
    
    
    from itertools import permutations
    
    
    s = "ABCDEFG"
    
    perms = (''.join(t) for t in permutations(s, len(s)))
    perms = sorted(set(perms))
    #print(perms, len(perms))
    
    
    
    from time import perf_counter
    
    t = perf_counter()
    for i,p in enumerate(perms):
        len(p) == len(set(p))
        assert rank(p) == i
        #print(p, i, ix)
    t1 = perf_counter() - t
    
    t = perf_counter()
    for i,p in enumerate(perms):
        assert rank_repetition(p) == i
        #print(p, i, ix)
    t2 = perf_counter() - t
    
    print(t1, t2)
