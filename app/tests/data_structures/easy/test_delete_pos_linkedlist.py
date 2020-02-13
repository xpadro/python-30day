from data_structures.easy.delete_pos_linkedlist import deleteNode, SinglyLinkedList

def build_list(node):
    result = []

    while node:
        result.append(node.data)

        node = node.next
    
    return result


def test_deleteNode():
    llist = SinglyLinkedList()
    llist.insert_node(20)
    llist.insert_node(6)
    llist.insert_node(2)
    llist.insert_node(19)
    llist.insert_node(7)
    llist.insert_node(4)
    llist.insert_node(15)
    llist.insert_node(9)

    head = deleteNode(llist.head, 3)

    assert build_list(head) == [20, 6, 2, 7, 4, 15, 9], "Should be [20, 6, 2, 7, 4, 15, 9]"