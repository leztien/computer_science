"""
binary search
"""

from random import randint


def make_search_space(n, max_value=None):
    max_value = int(max_value or n*2)
    return tuple(sorted(randint(0, max_value) for _ in range(n)))
    
  
def binarysearch(seq, item):
    lo, hi = 0, len(seq) - 1
    while not (lo > hi):
        ix = (lo+hi) // 2
        if seq[ix] == item:
            return True
        
        if item < seq[ix]:
            hi = ix - 1
        elif item > seq[ix]:
            lo = ix + 1
    return False


def iterative_binary_search(seq, item):
    while True:
        ix = len(seq) // 2
                
        if seq[ix] == item:
            return True
        
        if item < seq[ix] and ix > 0:
            seq = seq[:ix]
        elif item > seq[ix] and ix < len(seq) - 1:
            seq = seq[ix+1:]
        else:
            return False
        
        
        
def recursive_binary_search(seq, item, lo=None, hi=None):
    lo = lo or 0
    hi = len(seq)-1 if hi is None else hi
    m = (lo + hi) // 2
    
    # Base Case
    if item == seq[m]:
        return m
    
    # if "overflow" then return -1 (not found)
    if lo > hi: return -1
    
    # Recursive Case
    if item < seq[m]:
        hi = m - 1
    elif item > seq[m]:
        lo = m + 1
    # recursion
    return recursive_binary_search(seq, item, lo, hi)

        
    

def recursive_binary_search_from_geeksforgeeks(arr, item, low, high):
    # from https://www.geeksforgeeks.org/python-program-for-binary-search/
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == item:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > item:
            return recursive_binary_search_from_geeksforgeeks(arr, item, low, mid - 1)
 
        # Else the element can only be present in right subarray
        else:
            return recursive_binary_search_from_geeksforgeeks(arr, item, mid + 1, high)
 
    else:
        # Element is not present in the array
        return -1




if __name__ == '__main__':
    for _ in range(1000):
        print()
        n = randint(2, 20)
        seq = make_search_space(n)
        item = seq[randint(0, len(seq)-1)] if randint(0,1) else -1
        ans = recursive_binary_search(seq, item)
        
        # a little bit hackish
        print("item =", item, seq[ans] if item in seq else -1, seq, "index =", ans, seq.index(item) if item in seq else -1, item==seq[ans] if item != -1 else item == ans)
        
        if (item ==-1 and ans != -1):
            raise Exception(f"item={item}\t\tseq={seq} (1)")
        if item == ans:
            continue
        if (item != seq[ans]):
            raise Exception(f"item={item}\t\tseq={seq} (2)")
