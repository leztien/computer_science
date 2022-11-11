
"""
Linked List
"""


class Node:
    __slots__ = ('value', 'next')
    def __init__(self):
        self.value = None
        self.next = None
    
    
class LinkedList:
    def __init__(self, *values):
        self.head = node = Node()
        for value in values:
            node.value = value
            next = Node()
            node.next = next
            node = next
            
    def __iter__(self):
        node = self.head
        while node.next:
            yield node.value
            node = node.next
        
    def __repr__(self):
        return self.__class__.__name__ + str(tuple(self))

    def __len__(self):
        return sum(1 for e in self)
    
    # Access  O(n)
    def __getitem__(self, index):
        if not type(index) is int or index < 0:
            raise IndexError("bad index")
        
        node = self.head
        for i in range(index):
            node = node.next
            if node.next is None:
                raise IndexError("index out of range")
        return node.value
    
    # Search  O(n)
    def __contains__(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False
    
    # Search and return index
    def index(self, value):
        for i,v in enumerate(self):
            if v == value:
                return i
        return -1
    
    # Insertion  O(1)   insert at the head
    def push(self, value):
        node, self.head = self.head, Node()
        self.head.next, self.head.value = node, value

    # deletion O(1)    pop at the head
    def pop(self):
        self.head = self.head.next
    
    def insert(self, index, value):
        if index == 0:
            self.push(value)
            return
        node = self.head
        for _ in range(index-1):
            node = node.next
            if node.next.next is None:
                raise IndexError("bad index")
        new = Node()
        new.value = value
        new.next, node.next = node.next, new
        
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.head
        for _ in range(index-1):
            node = node.next  # BUG
            if node.next.next is None:
                raise IndexError("bad index")
        node.next = node.next.next
        
    

class DoublyLinkedList:
    ...
    # make an Abstract ?









if __name__ == '__main__':
    l = LinkedList(10, 0, 3, -7, 42)
    print(l)



