class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        toInsert = Node(value)

        if self.root is None:
            self.root = toInsert
        else:
            self.__insertNode(toInsert, self.root)

    def lookup(self, value):
        current_node = self.root

        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return current_node.value
        
        return None

    def __insertNode(self, toInsert, node):
        if toInsert.value < node.value:
            if node.left is None:
                node.left = toInsert
            else:
                self.__insertNode(toInsert, node.left)
        else:
            if node.right is None:
                node.right = toInsert
            else:
                self.__insertNode(toInsert, node.right)
    