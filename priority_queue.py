

"""
Priority Queue implemented with a binary heap
https://www.youtube.com/watch?v=eVq8CmoC1x8&t=68s
"""


class Heap:
    """
    Binary heap (no frills)
    """
    def __init__(self):
        self._nodes = []
    
    def __len__(self):
        return len(self._nodes)
    
    def is_empty(self):
        return len(self._nodes) == 0

    def add(self, item):
        # alias for convenience
        nodes = self._nodes
        
        # append to the end
        nodes.append(item)
        
        # bubble up
        c = len(nodes) - 1
        while c:
            p = (c - (1 if c%2 else 2)) // 2
            if nodes[c] < nodes[p]:
                nodes[c], nodes[p] = nodes[p], nodes[c]
                c = p
            else:
                break
    
    def top(self):
        """returns the top element but does not remove it, unlike pop()"""
        return self._nodes[0]
    
    def pop(self):
        # alias for convenience
        nodes = self._nodes
        
        # swap
        nodes[0], nodes[-1] = nodes[-1], nodes[0]
        
        # pop
        item = nodes.pop()
        
        # bubble down
        p = 0
        while True:
            # determine the indeces
            l = (2*p + 1) if (2*p + 1) < len(nodes) else None
            r = (2*p + 2) if (2*p + 2) < len(nodes) else None
            c = r if (l and r) and (nodes[r] < nodes[l]) else l
            
            # swap if necessary
            if c and nodes[c] < nodes[p]:
                nodes[p], nodes[c] = nodes[c], nodes[p]
                p = c
            else: break
        return item
        

# DEMO / TEST
if __name__ == '__main__':
    from random import randint, shuffle
    
    heap = Heap()
    
    for _ in range(randint(1, 100)):
        heap.add(randint(0, 100))
    
    ls = [heap.pop() for _ in range(len(heap))]
    
    print(ls, ls == sorted(ls))
    




