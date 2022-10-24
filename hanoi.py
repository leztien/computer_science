import array
class Stack:
    def __init__(self):
        self._stack = array.array('i')
    
    def push(self, value):
        self._stack.append(value)
        
    def pop(self):
        return self._stack.pop()
    
    def __len__(self):
        return len(self._stack)
    
    @property
    def is_sorted(self):
        return self._stack.tolist() == sorted(self._stack)
    
    def __str__(self):
        return str(self.__class__.__name__ + '(' + self._stack.tolist().__str__()[1:-1] + ')')
    def __repr__(self):
        return self.__str__()

#==========================================================================    

import inspect
def solve_tower_of_hanoi(A, B, C, n):
    """A = start    B = intermediate   C = destination"""
    
    #check restrictin (no bigger disc on top a smaller one)
    booleans = [stack.is_sorted for stack in (A, B, C)]
    assert all(booleans),"towers must be in assedning order!"

    #base case
    if n == 1:
        C.push(A.pop())
    
    #general case
    else:
        this = globals().get(inspect.stack()[0].function)
        this(A,C,B, n-1)
        this(A,B,C, 1)
        this(B,A,C, n-1)
        
#############################################################################################

n_towers, n_discs = 3, 5

A,B,C = (Stack() for _ in range(n_towers))
[A.push(disc) for disc in range(1, n_discs+1)]

print("before:", A, B, C)
solve_tower_of_hanoi(A, B, C, n=len(A))
print("after: ", A, B, C)
