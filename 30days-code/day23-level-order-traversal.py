from collections import deque

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = deque()
        visited = deque()

        if root is not None:
            visited.append(root)
            self.visitNode(queue, visited)

        result = ' '.join([str(x.data) for x in queue])
        print(result)



    def visitNode(self, queue, visited):
        if len(visited) == 0:
            return queue

        node = visited.popleft()
        queue.append(node)
        
        if node.left is not None:
            visited.append(node.left)
        
        if node.right is not None:
            visited.append(node.right)
        
        self.visitNode(queue, visited)
        


T=int(input())
myTree=Solution()
root=None

for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)

myTree.levelOrder(root)