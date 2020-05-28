from data_structures.linkedlist.doublylinkedlist import DoublyLinkedList, DoublyLinkedListNode

def test_linkedlist():
    linkedlist = DoublyLinkedList(5)

    assert linkedlist.head.value == 5, "Should be 5"
    assert linkedlist.size == 1, "Should be size of 1"

def test_append():
    linkedlist = DoublyLinkedList(5)
    linkedlist.append(8)

    assert linkedlist.head.value == 5, "Should be 5"
    assert linkedlist.head.next.value == 8, "Should be 8"
    assert linkedlist.tail.value == 8, "Should be 8"

    assert linkedlist.size == 2, "Should be size of 2"
    assert linkedlist.print() == [5, 8], "list should be [5, 8]"

def test_prepend():
    linkedlist = DoublyLinkedList(5)
    linkedlist.prepend(8)

    assert linkedlist.head.value == 8, "Should be 8"
    assert linkedlist.head.next.value == 5, "head.next should be 5"
    assert linkedlist.tail.value == 5, "tail should be 5"

    assert linkedlist.size == 2, "Should be size of 2"
    assert linkedlist.print() == [8, 5], "list should be [8, 5]"

def test_insert():
    linkedlist = DoublyLinkedList(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(5)

    linkedlist.insert(3, 4)

    assert linkedlist.print() == [1, 2, 3, 4, 5], "list should be [1, 2, 3, 4, 5]"
    assert linkedlist.size == 5, "Should be size of 5"

def test_insert_bigger_index():
    linkedlist = DoublyLinkedList(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(5)

    linkedlist.insert(99, 4)

    assert linkedlist.print() == [1, 2, 3, 5, 4], "list should be [1, 2, 3, 5, 4]"
    assert linkedlist.size == 5, "Should be size of 5"

def test_delete():
    linkedlist = DoublyLinkedList(1)
    linkedlist.append(2)
    linkedlist.append(3)
    linkedlist.append(5)

    linkedlist.delete(2)

    assert linkedlist.print() == [1, 2, 5], "list should be [1, 2, 5]"
    assert linkedlist.size == 3, "Should be size of 3"