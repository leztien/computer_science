
"""
my function that return combinations
same functionality as itertools.combinations
(maybe a more elegant implementation is possible)
"""


def get_combinations(seq, r):
    
    combinations = []
    
    def recurse(s, r, depth = 0):
        if depth == r:
            combinations.append([])
            return

        mx = (-r+1) + depth if (-r+1) + depth !=0 else len(s)
        
        for i,e in enumerate( s[0: mx] ):
            recurse(s[1+i:], r, depth+1)
            
            for combination in combinations:
                if len(combination) == r - depth - 1:
                    combination.append(e)
    recurse(seq, r)
    return tuple(tuple(e)[::-1] for e in combinations)
        


# test
if __name__ == "__main__":
    from itertools import combinations
    from random import randint
    from string import ascii_uppercase as abc
    
    
    for test in range(20):
        print()
        mx = 15
        n = randint(2, mx)
        r = randint(2, n)
        
        if randint(0,1):
            seq = abc[:n]
        else:
            seq = list(range(n))
        
        print(f"test {test+1}, n = {n}, r = {r}")
        print("seq =", seq)
        
        ist = get_combinations(seq, r)
        soll = tuple(combinations(seq, r))
        
        passed = sorted(ist) == sorted(soll)
        print(passed)
        if not passed:
            raise Exception("failed")



