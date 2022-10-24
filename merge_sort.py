
from math import inf


from random import randint
m = randint(0, 100)
a = [randint(0, randint(0,100)) for _ in range(m)]
print(a)


def merge_sort(a):
    #base case
    if len(a) == 1: return a    
    
    #non-base case
    mid = len(a) // 2
    L = a[:mid]
    R = a[mid:]
    
    L = merge_sort(L)
    R = merge_sort(R)
    
    M = merge(L,R,a)  # M = merged 
    return M




def merge(L,R,a):
    l,r = 0,0   # moving indeces
    for i in range(len(a)):
        l_val = L[l] if l < len(L) else inf
        r_val = R[r] if r < len(R) else inf
        
        if l_val < r_val:
            a[i] = L[l]
            l+=1
        else:
            a[i] = R[r]
            r+=1
    return a



arr = merge_sort(a)
print(arr)
print(arr==(sorted(a)))
