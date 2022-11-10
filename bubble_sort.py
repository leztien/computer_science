
"""
bubble sort
"""

from random import randint

def make_seq(n, max_value=None):
    max_value = int(max_value or n*2)
    return [randint(0, max_value) for _ in range(n)]



def bubblesort(s: list):
    while True:
        flag = True  # True = the list is sorted
        for i in range(0, len(s)-1):  # the last index not inclusive
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
                flag = False  # i.e. not sorted
        if flag == True:
            return  # this algorithm sorts a list in-place


# alternative:
def bubblesort(l):
    sorted = False
    while not sorted:
        sorted = True  # assume l is sorted
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                sorted = False
                
                
if __name__ == '__main__':
    seq = make_seq(10)
    print("BEFORE:", seq)
    
    bubblesort(seq)
    print("AFTER: ", seq, seq == sorted(seq))
