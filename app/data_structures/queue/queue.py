class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None

class Queue:
    """ Queue implementation
    
    """


    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def enqueue(self, value):
        node = Node(value)
        
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            self.first.previous = node
            self.first = node
        
        self.size = self.size + 1
        
    
    def dequeue(self):
        if self.last == None:
            return None
            
        last = self.last
        self.last = self.last.previous
        self.size = self.size - 1

        return last.value
    
    def peek(self):
        return self.last.value
    
    def print(self):
        result = []
        current = self.last

        while current is not None:
            result.append(current.value)
            current = current.previous
        
        return result