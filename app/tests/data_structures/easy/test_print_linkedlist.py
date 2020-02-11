from data_structures.easy.print_linkedlist import iterateItems,SinglyLinkedListNode,SinglyLinkedList

def test_iterateItems():
    llist = SinglyLinkedList()
    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)

    assert iterateItems(llist.head) == [1, 2, 3], "Should be [1, 2, 3]"