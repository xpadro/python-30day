class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)

        node.next = self.top
        self.top = node
        self.size = self.size + 1

    def pop(self):
        if self.top == None:
            return None
        
        result = self.top
        self.top = self.top.next
        self.size = self.size - 1
        return result.value

    def peek(self):
        return self.top.value
    
    def print(self):
        current = self.top
        result = []

        while (current is not None):
            result.append(current.value)
            current = current.next
        
        return result
