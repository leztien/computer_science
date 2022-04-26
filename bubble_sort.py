
"""
bubble sort
"""

from random import randint

def make_seq(n, max_value=None):
    max_value = int(max_value or n*2)
    return [randint(0, max_value) for _ in range(n)]



def bubble_sort(seq):
    while True:
        is_sorted = True
        for ix in range(0, len(seq)-1):
            if seq[ix] > seq[ix+1]:
                seq[ix], seq[ix+1] = seq[ix+1], seq[ix]
                is_sorted = False
        if is_sorted:
            return  # sorts a list in-place


if __name__ == '__main__':
    seq = make_seq(10)
    print("BEFORE:", seq)
    
    bubble_sort(seq)
    print("AFTER: ", seq, seq == sorted(seq))
