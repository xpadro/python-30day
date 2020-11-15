from data_structures.linkedlist.delete_duplicate import SinglyLinkedListNode, SinglyLinkedList, removeDuplicates

def test_removeDuplicates():
    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(2)
    llist1.insert_node(2)
    llist1.insert_node(3)
    llist1.insert_node(3)

    head = removeDuplicates(llist1.head)

    assert head.data == 1
    assert head.next.data == 2
    assert head.next.next.data == 3
    assert head.next.next.next == None