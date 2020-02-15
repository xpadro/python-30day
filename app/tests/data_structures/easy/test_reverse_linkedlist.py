from data_structures.easy.reverse_linkedlist import reversePrint, SinglyLinkedList
from utils.capture_output import capture_stdout


def test_reverseList():
    llist = SinglyLinkedList()
    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)
    llist.insert_node(4)
    llist.insert_node(5)

    output = capture_stdout(reversePrint, [llist.head])

    assert output == "5\n4\n3\n2\n1", "Should be 5\n4\n3\n2\n1"