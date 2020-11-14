from data_structures.linkedlist.node_value import SinglyLinkedListNode, SinglyLinkedList, getNode

def test_merge():
    llist1 = SinglyLinkedList()
    llist1.insert_node(3)
    llist1.insert_node(2)
    llist1.insert_node(1)

    result = getNode(llist1.head, 2)

    assert result == 3


    llist1 = SinglyLinkedList()
    llist1.insert_node(1)

    result = getNode(llist1.head, 0)

    assert result == 1


    llist1 = SinglyLinkedList()
    llist1.insert_node(86)
    llist1.insert_node(48)
    llist1.insert_node(91)
    llist1.insert_node(93)
    llist1.insert_node(79)
    llist1.insert_node(87)
    llist1.insert_node(27)
    llist1.insert_node(79)
    llist1.insert_node(67)
    llist1.insert_node(41)
    llist1.insert_node(8)
    llist1.insert_node(1)
    llist1.insert_node(95)
    llist1.insert_node(2)
    llist1.insert_node(14)
    llist1.insert_node(62)
    llist1.insert_node(35)
    llist1.insert_node(2)
    llist1.insert_node(2)
    llist1.insert_node(59)
    llist1.insert_node(17)
    llist1.insert_node(51)
    llist1.insert_node(19)
    llist1.insert_node(20)
    llist1.insert_node(17)
    llist1.insert_node(69)
    llist1.insert_node(69)
    llist1.insert_node(24)
    llist1.insert_node(14)
    llist1.insert_node(21)
    llist1.insert_node(58)
    llist1.insert_node(52)
    llist1.insert_node(68)
    llist1.insert_node(100)
    llist1.insert_node(44)

    result = getNode(llist1.head, 0)

    assert result == 44
    
