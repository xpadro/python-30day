from data_structures.easy.insert_pos_linkedlist import insertNodeAtPosition,SinglyLinkedListNode,SinglyLinkedList,print_singly_linked_list

def build_list(node):
    result = []

    while node:
        result.append(node.data)

        node = node.next
    
    return result


def test_insertNodeAtPosition():
    llist = SinglyLinkedList()
    head = insertNodeAtPosition(llist.head, 1, 5)
    head = insertNodeAtPosition(head, 2, 1)
    head = insertNodeAtPosition(head, 3, 1)
    head = insertNodeAtPosition(head, 4, 0)

    assert build_list(head) == [4, 1, 3, 2], "Should be [4, 1, 3, 2]"