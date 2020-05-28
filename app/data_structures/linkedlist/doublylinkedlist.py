class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self, value):
        node = DoublyLinkedListNode(value)
        self.head = node
        self.tail = node
        self.size = 1
    
    def append(self, value):
        node = DoublyLinkedListNode(value)

        self.tail.next = node
        node.previous = self.tail
        self.tail = node
        self.size = self.size + 1

    def prepend(self, value):
        node = DoublyLinkedListNode(value)
        node.next = self.head
        self.head.previous = node
        self.head = node
        self.size = self.size + 1

    def insert(self, position, value):
        if position == 0:
            self.prepend(value)
            return
        
        if position >= self.size:
            self.append(value)
            return
        
        found_node = self.__findNode(position)
        
        if found_node is not None:
            node = DoublyLinkedListNode(value)
            node.next = found_node
            node.previous = found_node.previous

            found_node.previous.next = node
            found_node.previous = node
            
            self.size = self.size + 1

    def delete(self, position):
        if position >= self.size:
            return
        
        to_delete = self.__findNode(position)

        if to_delete is not None:
            to_delete.next.previous = to_delete.previous
            to_delete.previous.next = to_delete.next
            
            to_delete = None
            self.size = self.size - 1


    def __findNode(self, position):
        index = 0
        current = self.head

        while index < position and current is not None:
            current = current.next
            index = index + 1
        
        return current

    def print(self):
        current = self.head
        result = []

        while current is not None:
            result.append(current.value)
            current = current.next
        
        return result

