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

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
# 1 -> 2 -> 2 -> 3
def removeDuplicates(head):
    fixed_head = head
    prev_node = head

    while head is not None:
        if head.next is None:
            prev_node.next = None
            break
        
        head = head.next

        if prev_node.data != head.data:
            prev_node.next = head
            prev_node = head
    
    return fixed_head

