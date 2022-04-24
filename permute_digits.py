


def permute_digits(n_digits, digits_list=None):
    def recurse(perm, depth=0):
        # base case
        if depth == len(perm):
            return
        
        # recursive case
        for digit in digits_list:
            perm[depth] = digit
            recurse(perm, depth=depth+1)
            
            # patch because of a bug
            if seq and seq[-1] == tuple(perm):
                continue
            
            seq.append(tuple(perm))
            
        if seq and depth == 0:
            return seq
        
    digits_list = digits_list or tuple(range(10))
    seq = []
    return recurse([0] * n_digits)
        
   


if __name__ == '__main__':           
    l = permute_digits(2, "0123456789ABCDEF")
    print(l)
    
    l = [str.join('', (str(e) for e in t)) for t in l]
    print(l)
    
    l = [int(e, base=16) for e in l]
    print(l)

