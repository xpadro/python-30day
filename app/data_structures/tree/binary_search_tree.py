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
    
        return None

    def __insertNode(self, toInsert, node):
        print("Value: " + str(toInsert.value) + " | at node: " + str(node.value))

        if toInsert.value < node.value:
            if node.left is None:
                print("insert value " + str(toInsert.value) + " at left node " + str(node.value))
                node.left = toInsert
            else:
                self.__insertNode(toInsert, node.left)
        else:
            if node.right is None:
                print("insert value " + str(toInsert.value) + " at right node " + str(node.value))
                node.right = toInsert
            else:
                self.__insertNode(toInsert, node.right)
        

    def lookup(self, value):
        None