"""
quick and dirty implementation of Linked List
"""

class Node:
    def __init__(self):
        self.value = None
        self.next = None

        
        
class LinkedList:
    def __init__(self, values):
        self.first = node = Node()
        for value in values:
            node.value = value
            next = Node()
            node.next = next
            node = next
            
            
    def __iter__(self):
        next = self.first
        while next.value:
            yield next.value
            next = next.next
    
    def __str__(self):
        t = tuple(self)
        return "<{}>".format(str(t)[1:-1])
    def __repr__(self):
        return self.__str__()
    
    def _get_node(self, ix):
        next = self.first
        for i in range(ix):
            try: next = next.next
            except AttributeError:
                raise IndexError("index out of range")
        if next is None or next.value is None:
            raise IndexError("index out of range")
        return next
    
    def __getitem__(self, ix):
        node = self._get_node(ix)
        return node.value


    def __setitem__(self, ix, value):
        node = self._get_node(ix)
        node.value = value
        
    
    def delete(self, ix):
        if ix==0:
            self.first = self.first.next
        else:
            node = self.first
            for i in range(ix-1):
                node = node.next
            node.next = node.next.next
    
    def insert(self, ix, value):
        new = Node()
        new.value = value
        if ix==0:
            new.next = self.first
            self.first = new
        else:
            node = self._get_node(ix-1)
            new.next = node.next
            node.next = new
            
    

l = LinkedList([10,20,30,"A","B","C", "xyz"])
for e in l:
    print(e)

print(l)
