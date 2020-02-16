from data_structures.easy.reverse_linkedlist import reverse, SinglyLinkedList
from utils.utils import build_list


def test_reverseList():
    llist = SinglyLinkedList()
    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)
    llist.insert_node(4)
    llist.insert_node(5)

    result = reverse(llist.head)

    assert build_list(result) == [5, 4, 3, 2, 1], "Should be [5, 4, 3, 2, 1]"