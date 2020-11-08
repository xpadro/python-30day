import math
import os
import random
import re
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


def mergeLists(head1, head2):
    """ Merges two sorted linked list into a new sorted list (HackerRank version)

    """

    if not head1:
        return head2
    
    if not head2:
        return head1

    result = SinglyLinkedList()

    if head1.data < head2.data:
        result.insert_node(head1.data)
        head1 = head1.next
    else:
        result.insert_node(head2.data)
        head2 = head2.next

    
    while head1 is not None or head2 is not None:
        if not head1:
            result.insert_node(head2.data)
            head2 = head2.next
        elif not head2:
            result.insert_node(head1.data)
            head1 = head1.next
        else:
            if head1.data < head2.data:
                result.insert_node(head1.data)
                head1 = head1.next
            else:
                result.insert_node(head2.data)
                head2 = head2.next
        
    return result.head
        