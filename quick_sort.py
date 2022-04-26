
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
    



if __name__ == '__main__':
    seq = make_seq(10)
    print("BEFORE:", seq)
    
    output = quick_sort(seq)
    print("AFTER: ", output, output == sorted(output))
