class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """ Linked List implementation
    
    """


    def __init__(self, value):
        node = LinkedListNode(value)
        self.head = node
        self.tail = node
        self.size = 1
    
    def append(self, value):
        node = LinkedListNode(value)

        self.tail.next = node
        self.tail = node
        self.size = self.size + 1

    def prepend(self, value):
        node = LinkedListNode(value)
        node.next = self.head
        self.head = node
        self.size = self.size + 1

    def insert(self, position, value):
        if position == 0:
            self.prepend(value)
            return
        
        if position >= self.size:
            self.append(value)
            return
        
        found_node = self.__findPreviousNode(position)
        
        if found_node is not None:
            node = LinkedListNode(value)
            node.next = found_node.next
            found_node.next = node
            self.size = self.size + 1

    def delete(self, position):
        if position >= self.size:
            return
        
        found_node = self.__findPreviousNode(position)

        if found_node is not None:
            to_delete = found_node.next
            found_node.next = to_delete.next
            to_delete = None
            self.size = self.size - 1


    def __findPreviousNode(self, position):
        index = 0
        current = self.head
        previous = None

        while index < position and current is not None:
            previous = current
            current = current.next
            index = index + 1
        
        return previous

    def print(self):
        current = self.head
        result = []

        while current is not None:
            result.append(current.value)
            current = current.next
        
        return result

