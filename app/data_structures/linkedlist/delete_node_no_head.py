class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def delete(node: ListNode):
    """ Delete the given node from the linked list

    We don't have a reference to the head, so we can't update the previous node 'next' value. Instead,
    we update the value of the given node to become the next one

    """

    node.val = node.next.val
    node.next = node.next.next