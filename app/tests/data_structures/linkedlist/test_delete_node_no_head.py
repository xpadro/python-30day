from data_structures.linkedlist.delete_node_no_head import delete, ListNode

def test_delete_node():
    head = ListNode(4)
    n1 = ListNode(5)
    n2 = ListNode(1)
    n3 = ListNode(9)

    n2.next = n3
    n1.next = n2
    head.next = n1

    delete(n2)

    assert head.val == 4
    assert head.next.val == 5
    assert n1.next.val == 9
