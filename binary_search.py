
"""
binary search
"""

from random import randint

def make_search_space(n, max_value=None):
    max_value = int(max_value or n*2)
    return tuple(sorted(randint(0, max_value) for _ in range(n)))
    


def binary_search(seq, item):
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
    


if __name__ == '__main__':
    for _ in range(1000):
        seq = make_search_space(10)
        item = seq[randint(0, len(seq)-1)] if randint(0,1) else -1
        ans = binary_search(seq, item=item)
        print(item, seq, ans)
        if ans != (item in seq):
            raise Exception(f"item={item}\tseq={seq}")



