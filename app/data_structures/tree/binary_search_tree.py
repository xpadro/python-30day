class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """ Binary Search Tree implementation

    """


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

    def bfs(self):
        """ Breadth-first search

        """


        result = []
        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            result.append(current.value)

            if current.left is not None:
                queue.append(current.left)
            
            if current.right is not None:
                queue.append(current.right)
        
        return result
    
    def dfs(self):
        """ Depth-first search
        
        """


        return self.__dfs(self.root, [])

    def __dfs(self, node, result):
        if node is not None:
            result.append(node.value)

            result = self.__dfs(node.left, result)
            result = self.__dfs(node.right, result)

        return result

            

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
    