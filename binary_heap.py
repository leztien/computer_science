
"""
quick and dirty (i.e. experimental) Binary Heap implementation

continue:
https://runestone.academy/ns/books/published//pythonds/Trees/BinaryHeapImplementation.html
"""


from math import log2, floor
from random import randint


import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout



def draw_tree(list):
    l = list
    n_levels = floor(log2(len(l)))
    n_nodes = 2**(n_levels+1)-1
    T = nx.balanced_tree(2, n_levels)
    for e in range(n_nodes-1, len(l)-1, -1):
        T.remove_node(e)
    labels = {k:str(v) for k,v in enumerate(l)}
    pos = graphviz_layout(T, prog="dot")
    nx.draw(T, pos, with_labels=False, node_color='lightgreen')
    nx.draw_networkx_labels(T, pos, labels=labels, font_size=12, font_weight='bold')
    plt.show()




class BinaryHeap:
    def __init__(self):
        self._list = [0]
    
    def push(self, value):
        self._list.append(value)
        if len(self._list) < 3:
            return
        
        child = len(self._list) - 1
        parent = child // 2
        
        while parent > 0:
            if self._list[child] < self._list[parent]:
                self._list[child], self._list[parent] = self._list[parent], self._list[child]
                child = parent
                parent = child // 2
            else:
                break
        self._check_order()
    
    
    def pop(self):
        popped_value = self._list[1]
        self._list[1] = self._list.pop()
        
        ...
        
        
        
    def _check_order(self):
        l = self._list
        n = len(self._list)-1
        if n <= 1:
            return
        
        def recurse(index=1):
            # base case
            if index * 2 > n:
                return
            # recursive case
            parent = l[index]
            left = l[index*2]
            right = index*2+1
            right = l[right] if right <= n else float('inf')
            
            if (parent >  left) or (parent > right):
                print("ERROR: parent, left, right:", parent, left, right)
                self.draw()
                raise ValueError()

            recurse(index=index*2)
            recurse(index=index*2+1)
        recurse()
    
    
    def __repr__(self):
        return f"BinaryHeap({str(self._list[1:])[1:-1]})"
    def __str__(self):
        return self.__repr__()
        
    def draw(self):
        draw_tree(self._list[1:])




heap = BinaryHeap()

n_values = randint(1, 25)
for _ in range(n_values):
    heap.push(randint(0, n_values*3))





heap.draw()
print(heap)

