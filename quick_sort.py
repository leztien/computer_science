
"""
quick sort
"""

from random import randint

def make_seq(n, max_value=None):
    max_value = int(max_value or n*2)
    return [randint(0, max_value) for _ in range(n)]



def quick_sort(seq):
    # base case
    if len(seq) <= 1:
        return seq
    
    # recursive case
    pivot = seq[0]   # arbitrary value from the current list
    less, equal, greater = list(), list(), list()
    
    # go over each item, sort into the three lists
    for item in seq:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            greater.append(item)
        else:
            equal.append(item)
    
    # binary recursion
    return quick_sort(less) + equal + quick_sort(greater)
    


# terse version
from operator import eq, gt, lt

def quicksort(s):
    # Base Case
    if len(s) <= 1: return s
    
    # Recursive Case
    p = s[0]
    d = {lt: [], eq: [], gt: []}

    for e in s:
        for f, l in d.items():
            [l.append(e) if f(e, p) else None]
    
    return quicksort(d[lt]) + d[eq] + quicksort(d[gt])



if __name__ == '__main__':
    seq = make_seq(10)
    print("BEFORE:", seq)
    
    output = quick_sort(seq)
    print("AFTER: ", output, output == sorted(output))
