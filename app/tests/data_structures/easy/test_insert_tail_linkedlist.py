from data_structures.easy.insert_tail_linkedlist import insertNodeAtTail,SinglyLinkedListNode,SinglyLinkedList,print_singly_linked_list

def build_list(node):
    result = []

    while node:
        result.append(node.data)

        node = node.next
    
    return result


def test_insertNodeAtTail():
    llist = SinglyLinkedList()
    head = insertNodeAtTail(llist.head, 1)
    head = insertNodeAtTail(head, 2)
    head = insertNodeAtTail(head, 3)
    head = insertNodeAtTail(head, 4)

    assert build_list(head) == [1, 2, 3, 4], "Should be [1, 2, 3, 4]"
