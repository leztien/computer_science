"""
Linked List
"""


class Node:
    __slots__ = ('item', 'next', 'prev')
    def __init__(self):
        self.item = None
        self.next = None
        self.prev = None  # only for doubly linked list
    
    
class LinkedList:
    def __init__(self, *items):
        self.head = node = Node()
        for i,v in enumerate(items):
            node.item = v
            node.next = Node() if i < (len(items) - 1) else None
            node = node.next
            
    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next
        
    def __repr__(self):
        return self.__class__.__name__ + str(tuple(self))

    def __len__(self):
        return sum(1 for e in self)
    
    # Access  O(n)
    def __getitem__(self, index):
        if not(type(index) is int) or index < 0:
            raise IndexError("bad index")
        
        node = self.head
        for i in range(index):
            node = node.next
            if node is None:
                raise IndexError("index out of range")
        return node.item
    
    # Search  O(n)
    def __contains__(self, item):
        node = self.head
        while node is not None:
            if node.item == item:
                return True
            node = node.next
        return False
    
    # Search and return index
    def index(self, item):
        for i,v in enumerate(self):
            if v == item:
                return i
        return -1
    
    # Insertion  O(1)   insert at the head
    def push(self, item):
        node, self.head = self.head, Node()
        self.head.next, self.head.item = node, item

    # deletion O(1)    pop at the head
    def pop(self):
        self.head = self.head.next
    
    def insert(self, index, item):
        if index == 0:
            self.push(item)
            return
        node = self.head
        for _ in range(index-1):
            node = node.next
            if node.next.next is None:
                raise IndexError("bad index")
        new = Node()
        new.item = item
        new.next, node.next = node.next, new
        
    def delete(self, index):
        if index == 0:
            self.head = self.head.next
            return
        ...  #TODO
        
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        self.head = prev
        
    

class DoublyLinkedList:
    ...  #TODO
        

class Stack(LinkedList):
    def __init__(self, *items):
        """items are stored in reversed order for functionality"""
        super().__init__(*items[::-1])
    
    def __repr__(self):
        return self.__class__.__name__ + str(tuple(self)[::-1])
    
    def push(self, item):
        node = Node()
        node.item = item
        node.next = self.head
        self.head = node
    
    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        item = self.head.item
        self.head = self.head.next
        return item






##############################################

l = LinkedList(10, 20, 30, 40, 50)

s = Stack(*l)


