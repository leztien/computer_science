"""
Edit Distance Algorithms
"""


from string import ascii_lowercase as l
from random import randint

def make_strings(maxlen=15):
    """makes a string, returns the original and a mangled one"""
    s1 = [l[randint(0,25)] for _ in range(randint(3, maxlen))]
    s2 = s1.copy()
    n = len(s1)
    for _ in range(randint(0, n)):
        ix = randint(0,n-1)
        op = randint(1,3)
        if op == 1:
            del s2[ix]
        elif op == 2:
            s2[ix:ix] = l[randint(0,25)]
        else:
            s2[ix] = l[randint(0,25)]
        n = len(s2)
    
    s1,s2 = (str.join('', l) for l in (s1,s2))
    return s1,s2




import numpy as np

def edit_distance_tabular(s1, s2, replacement_cost=2):
    """edit distance with dinamic programming (second fastest here)"""
    m = len(s2)
    n = len(s1)
    
    D = np.zeros(shape=(m+1, n+1), dtype=np.uint16)
    D[:,0] = range(m+1)
    D[0,:] = range(n+1)
    
    # Fill in the table
    for i in range(1, m+1):
        for j in range(1, n+1):
            D[i,j] = min(D[i-1, j-1] + (0 if s1[j-1] == s2[i-1] else replacement_cost), 
                         D[i-1, j] + 1,
                         D[i, j-1] + 1)
    return D[m,n]




import inspect

def edit_distance_recursive_naive(s1, s2, replacement_cost=2):
    """innefficient algorithm which explores all paths"""
    # Get this function
    f = globals().get(inspect.stack()[0].function)
    
    # Base case
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    
    # Recursive case
    return min(
    f(s1[:-1], s2[:-1], replacement_cost=replacement_cost) + (0 if s1[-1] == s2[-1] else replacement_cost),
    f(s1[:-1], s2, replacement_cost=replacement_cost) + 1,
    f(s1, s2[:-1], replacement_cost=replacement_cost) + 1
    )
    


def edit_distance_recursive_improved(s1, s2, replacement_cost=2):
    """redices redundancy"""
    # Get this function
    f = globals().get(inspect.stack()[0].function)
        
    # Base case
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    
    # recursive cases
    if s1[-1] == s2[-1]:
        return f(s1[:-1], s2[:-1], replacement_cost=replacement_cost)
     
    return min(
    f(s1[:-1], s2[:-1], replacement_cost=replacement_cost) + replacement_cost,
    f(s1[:-1], s2, replacement_cost=replacement_cost) + 1,
    f(s1, s2[:-1], replacement_cost=replacement_cost) + 1
    )
    


def edit_distance_recursive_cached(s1, s2, replacement_cost=2):
    """Stanford's Percy Liang (the fastest)"""
    
    # Cache for memoization
    cache = dict()
    
    # Inner recursive function
    def recurse(i, j, replacement_cost=2):
        # If cached - retrun from chache
        if (i,j) in cache: return cache[(i,j)]
        
        # Base case
        if i == 0: return j
        if j == 0: return i
        
        # If last letters are the same
        if s2[i-1] == s1[j-1]:
            ans = recurse(i-1, j-1, replacement_cost=replacement_cost)
            
        # If last letters differ
        else:
            sub_cost = recurse(i-1, j-1, replacement_cost=replacement_cost) + replacement_cost   # substitution cost
            ins_cost = recurse(i-1, j, replacement_cost=replacement_cost) + 1   # insertion cost
            del_cost = recurse(i, j-1, replacement_cost=replacement_cost) + 1   # deletion cost
            ans = min(sub_cost, ins_cost, del_cost)
        
        # Cache and return
        cache[(i,j)] = ans
        return ans
    return recurse(len(s2), len(s1), replacement_cost=replacement_cost)




def similarity_ratio(s1, s2):
    """Levenshtein similarity ratio"""
    d = edit_distance_recursive_cached(s1, s2, replacement_cost=2)  # must be 2 here !!!
    return (len(s1) + len(s2) - d) / (len(s1) + len(s2))




def get_suggestions(word, vocabulary=None, min_distance=1, replacement_cost = 1):
    vocabulary = vocabulary or globals().get('vocabulary')
    
    def condition(word, voc):
        return (
        word[0] == voc[0] and
        word != voc
        )
    
    distances = [0,] * len(vocabulary)
    
    for i,s in enumerate(vocabulary):
        distances[i] = edit_distance_recursive_cached(word, vocabulary[i], replacement_cost=replacement_cost)
    mn = max(min(distances), min_distance)
    
    suggestions = [vocabulary[i] for i in range(len(vocabulary)) if distances[i] <= mn and condition(word, vocabulary[i])]
    return suggestions




def n_grams_ratio(s1, s2, n=2):
    s1, s2 = (str(s).strip().lower() for s in (s1,s2))
    S1, S2 = (frozenset(s[i:i+n] for i in range(len(s)-1)) for s in (s1, s2))
    return len(S1.intersection(S2)) / len(S1.union(S2))


#####################################################################################


def main():
    import time
    
    # Levenshtein distance
    s1,s2 = make_strings(maxlen=5)
    
    replacement_cost = 2
    
    t1 = time.process_time()
    d1 = edit_distance_tabular(s1, s2, replacement_cost=replacement_cost)
    t1 = time.process_time() - t1
    
    t2 = time.process_time()
    d2 = edit_distance_recursive_naive(s1, s2, replacement_cost=replacement_cost)
    t2 = time.process_time() - t2
    
    t3 = time.process_time()
    d3 = edit_distance_recursive_improved(s1, s2, replacement_cost=replacement_cost)
    t3 = time.process_time() - t3
    
    t4 = time.process_time()
    d4 = edit_distance_recursive_cached(s1, s2, replacement_cost=replacement_cost)
    t4 = time.process_time() - t4
    
    print(s1,s2, d4, [round(n,5) for n in   (t1,t2,t3,t4)])
    assert d1==d2==d3==d4
    
    
    # Levenshtein ratio
    r = similarity_ratio(s1, s2)
    print(s1, s2, r)
    


    # Spellchecking suggestions
    import os
    PATH = os.path.expanduser("~/Datasets/1000_common_english_words.txt")
    with open(PATH, mode='rt', encoding='utf-8') as fr:
        vocabulary = fr.read().split('\n')
    
    words = ("pahe", "peeple", "piepl", "wurld", "gurl", "feind", "pleys", "litl", "recieve", "good")
    
    for word in words:
        print(word, get_suggestions(word, vocabulary))
        


    # Use Levenshtein distance in this case
    s = s1 = "California"
    options = ("CA", "DC", "KA", "AC", "NV")
    
    for s2 in options:
        r = similarity_ratio(s1, s2)
        print(s2, r)
    
    # Use N-Grams in this case:
    s = s1 = "Double Bedroom"
    options = ("Bedroom Double", "Double Room", "King bedroom", "Double bed room", "Room with a double bed")
    
    for s2 in options:
        r = n_grams_ratio(s1, s2, n=2)
        print(s2, r)
    
if __name__ == "__main__": main()



"""
read on fuzzy mathing here:
https://www.datacamp.com/community/tutorials/fuzzy-string-python
"""
