from data_structures.linkedlist.compare_linkedlists import SinglyLinkedListNode, SinglyLinkedList, compare_lists

def test_compare():
    llist1 = SinglyLinkedList()
    llist1.insert_node(1)

    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    assert compare_lists(llist1.head, llist2.head) == 1

    llist1 = SinglyLinkedList()
    llist2 = SinglyLinkedList()
    assert compare_lists(llist1.head, llist2.head) == 1

    llist1 = SinglyLinkedList()
    llist1.insert_node(1)

    llist2 = SinglyLinkedList()
    llist2.insert_node(0)
    assert compare_lists(llist1.head, llist2.head) == 0

    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(2)

    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    assert compare_lists(llist1.head, llist2.head) == 0

    llist1 = SinglyLinkedList()
    llist1.insert_node(1)

    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    llist2.insert_node(2)
    assert compare_lists(llist1.head, llist2.head) == 0