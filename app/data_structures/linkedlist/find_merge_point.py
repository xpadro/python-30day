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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    ''' Given two linked lists, it returns the value of the node where the two lists join (they both point to the same node reference)

    '''

    visited_nodes1 = []
    visited_nodes2 = []

    while head1 is not None or head2 is not None:
        if head1 is not None:
            visited_nodes1.append(head1)
            
            if head1 in visited_nodes2:
                return head1.data

            head1 = head1.next

        if head2 is not None:
            visited_nodes2.append(head2)

            if head2 in visited_nodes1:
                return head2.data
            
            head2 = head2.next
    
    return -1

