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

    def getHeight(self,root):
        #Write your code here
        max_height = 0
        if root is None:
            return max_height
        
        return self.calculateHeight(max_height, root)

    
    def calculateHeight(self, max_height, root):
        if root is None:
            return max_height - 1
        
        left_height = self.calculateHeight(max_height + 1, root.left)
        right_height = self.calculateHeight(max_height + 1, root.right)

        return max(left_height, right_height)






#T=int(input())
T = 7
myTree=Solution()
root=None
'''
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
'''

arr = [3, 5, 2, 1, 4, 6, 7]
for i in arr:
    data=int(i)
    root=myTree.insert(root,data)

height=myTree.getHeight(root)
print(height)
