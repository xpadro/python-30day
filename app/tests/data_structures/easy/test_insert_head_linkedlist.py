from data_structures.easy.insert_head_linkedlist import insertNodeAtHead,SinglyLinkedListNode,SinglyLinkedList,print_singly_linked_list

def build_list(node):
    result = []

    while node:
        result.append(node.data)

        node = node.next
    
    return result


def test_insertNodeAtHead():
    llist = SinglyLinkedList()
    head = insertNodeAtHead(llist.head, 1)
    head = insertNodeAtHead(head, 2)
    head = insertNodeAtHead(head, 3)
    head = insertNodeAtHead(head, 4)

    assert build_list(head) == [4, 3, 2, 1], "Should be [4, 3, 2, 1]"