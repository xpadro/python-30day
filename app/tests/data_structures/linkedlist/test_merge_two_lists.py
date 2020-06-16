from data_structures.linkedlist.merge_two_lists import ListNode, merge, print_list

def test_merge():
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    assert print_list(merge(l1, l2)) == [1, 1, 2, 3, 4, 4]

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1)
    assert print_list(merge(l1, l2)) == [1, 1, 2, 4]

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode()
    assert print_list(merge(l1, l2)) == [0, 1, 2, 4]

    l1 = ListNode(3)
    l2 = ListNode(1, ListNode(2, ListNode(4)))
    assert print_list(merge(l1, l2)) == [1, 2, 3, 4]

    l1 = None
    l2 = ListNode(1, ListNode(2, ListNode(3)))
    assert print_list(merge(l1, l2)) == [1, 2, 3]

    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = None
    assert print_list(merge(l1, l2)) == [1, 2, 3]
