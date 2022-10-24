from random import randint
m = randint(0, 100)
a = [randint(0, randint(0,100)) for _ in range(m)]
print(a)



def insertion_sort(a):
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            continue
        
        for ix in range(0, i):
            if a[i] < a[ix]:
                break
        
        temp = a[i]
        for j in range(i, ix, -1):
            a[j] = a[j-1]
        else: a[ix] = temp
    return a



a = insertion_sort(a)
print(a, a==sorted(a))
