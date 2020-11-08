from data_structures.linkedlist.merge_two_lists_hk import SinglyLinkedListNode, SinglyLinkedList, mergeLists

def test_merge():
    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(1)
    llist1.insert_node(4)

    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    llist2.insert_node(3)
    llist2.insert_node(4)

    head = mergeLists(llist1.head, llist2.head)

    assert head.data == 1
    assert head.next.data == 1
    assert head.next.next.data == 1
    assert head.next.next.next.data == 3
    assert head.next.next.next.next.data == 4
    assert head.next.next.next.next.next.data == 4


    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(2)
    llist1.insert_node(4)

    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    llist2.insert_node(3)
    llist2.insert_node(4)

    head = mergeLists(llist1.head, llist2.head)

    assert head.data == 1
    assert head.next.data == 1
    assert head.next.next.data == 2
    assert head.next.next.next.data == 3
    assert head.next.next.next.next.data == 4
    assert head.next.next.next.next.next.data == 4


    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(2)
    llist1.insert_node(4)

    llist2 = SinglyLinkedList()
    llist2.insert_node(1)

    head = mergeLists(llist1.head, llist2.head)

    assert head.data == 1
    assert head.next.data == 1
    assert head.next.next.data == 2
    assert head.next.next.next.data == 4


    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(2)
    llist1.insert_node(4)

    llist2 = SinglyLinkedList()

    head = mergeLists(llist1.head, llist2.head)

    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 4


    llist1 = SinglyLinkedList()
    llist1.insert_node(3)

    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    llist2.insert_node(2)
    llist2.insert_node(4)

    head = mergeLists(llist1.head, llist2.head)

    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 3
    assert head.next.next.next.data == 4


    llist2 = SinglyLinkedList()
    llist2.insert_node(1)
    llist2.insert_node(2)
    llist2.insert_node(3)

    head = mergeLists(None, llist2.head)

    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 3


    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(2)

    head = mergeLists(llist1.head, None)

    assert head.data == 1
    assert head.next.data == 2
