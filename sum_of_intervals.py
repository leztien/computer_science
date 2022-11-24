

"""Intervals Union"""


# my solution
def unite_intervals(inteval_1, interval_2):
    """
    makes a union of two (sorted) intervals if they overlap,
    otherwise returns None
    """
    (a1, b1), (a2, b2) = inteval_1, interval_2
    assert a1 <= a2, "the input intervals must be sorted"
    if b1 <= a2:
        return None
    return [min(a1, a2), max(b1, b2)]


def sum_of_intervals_(intervals):
    intervals = sorted(intervals, key=lambda arr: arr[0])
    
    for ix in range(-len(intervals)+1, 0):
        interval_union = unite_intervals(intervals[ix-1], intervals[ix])
        
        if interval_union:
            intervals.pop(ix-1)
            intervals[ix] = interval_union
        
    return sum(b-a for a,b in intervals)




# the elegant solution from Codewars
def sum_of_intervals(intervals):
    """
    Total length of intervals, considering the overlapping parts
    (which mustn't be counted twice).
    """
    # initialize the Sum to zero
    summ = 0
    
    # initialize the "peg" that will move down (i.e. right) the number line
    peg = float('-inf')
    
    for start, end in sorted(intervals):
        if peg < end:
            summ += end - max(start, peg)
            peg = end
    return summ
    


intervals = [[1,5], [7,12], [10,22], [22,33], [25,30]]

print(sum_of_intervals(intervals))
print(sum_of_intervals_(intervals))


