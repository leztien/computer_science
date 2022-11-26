
"""
permute a sequence (with or without repetitions)
"""

def permute(sequence):
    """returns all permutations of the 'sequence' in order"""
    if len(sequence) == 1:
        return [sequence]
    
    result = list()
    for i,e in enumerate(sequence):
        new = list(sequence)
        new.pop(i)
        
        for l in permute(new):
            result.append([e] + l)
    return result
