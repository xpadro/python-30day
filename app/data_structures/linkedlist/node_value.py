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

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    cursor = head
    counter = 0
    
    #3 -> 2 -> 1 -> None
    while head is not None:
        head = head.next
        
        # offset of positionFromTail. The cursor won't start moving until it reaches the offset
        # When the head reaches the tail, cursor will be tail minus offset (positionFromTail)
        if counter < positionFromTail:
            counter = counter + 1
        elif head is not None:
            cursor = cursor.next
    
    return cursor.data
        