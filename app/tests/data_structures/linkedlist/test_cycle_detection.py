from data_structures.linkedlist.cicle_detection import SinglyLinkedListNode, SinglyLinkedList, has_cycle

def test_merge():
    llist1 = SinglyLinkedList()
    llist1.insert_node(3)
    llist1.insert_node(1)
    llist1.insert_node(2)

    assert has_cycle(llist1.head) == 0


    llist1 = SinglyLinkedList()
    llist1.insert_node(3)
    llist1.insert_node(1)
    llist1.insert_node(2)
    llist1.insert_node(1)

    assert has_cycle(llist1.head) == 0

    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(1)

    assert has_cycle(llist1.head) == 0


    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(1)
    node = llist1.head.next
    llist1.head.next.next = node

    assert has_cycle(llist1.head) == 1
    