from data_structures.linkedlist.find_merge_point import SinglyLinkedListNode, SinglyLinkedList, findMergeNode

def test_merge():
    llist1 = SinglyLinkedList()
    llist1.insert_node(1)
    llist1.insert_node(2)
    llist1.insert_node(3)

    node_1 = llist1.head

    llist2 = SinglyLinkedList()
    llist2.head = node_1

    assert findMergeNode(llist1.head, llist2.head) == 1