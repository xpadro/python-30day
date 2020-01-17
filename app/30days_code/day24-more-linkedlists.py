class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head is not None and head.next is not None:
            next_item = head.next
            current_item = head

            while next_item is not None:
                if current_item.data == next_item.data:
                    current_item.next = next_item.next
                    next_item = None
                else:
                    current_item = next_item
                    
                next_item = current_item.next

        return head
                

mylist= Solution()
T=int(input())
head=None

for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)

head=mylist.removeDuplicates(head)
mylist.display(head)