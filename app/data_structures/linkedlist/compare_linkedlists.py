import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def compare_lists(llist1, llist2):
    """ Checks if two linked lists are equal

    """
    
    if not llist1 and not llist2:
        return 1
    
    if not llist1 or not llist2:
        return 0

    head1 = llist1
    head2 = llist2

    while head1 is not None:
        if head2 is None:
            return 0
        
        if head1.data != head2.data:
            return 0

        head1 = head1.next
        head2 = head2.next
    
    if head2:
        return 0
    else:
        return 1

    

