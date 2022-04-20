def fibonacci(n):
    a, b = 1, 1
    seq = [a,b]
    
    for _ in range(n):
        a, b = b, a+b
        seq.append(b)
    return seq[:n]


# or like this:
def fibonacci(n):
    l = []
    for i in range(n):
        if i < 2:
            l.append(1)
        else:
            l.append(l[i-2] + l[i-1])
    return l



ans = fibonacci(10)
print(ans, len(ans))
