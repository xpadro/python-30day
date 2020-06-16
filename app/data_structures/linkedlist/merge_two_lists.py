class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(l1:ListNode, l2:ListNode):
    """ Merges two sorted linked list into a new sorted list

    """

    if not l1:
        return l2
    
    if not l2:
        return l1

    head = None
    current = None

    if l1.val < l2.val:
        head = ListNode(l1.val)
        l1 = l1.next
    else:
        head = ListNode(l2.val)
        l2 = l2.next

    current = head
    
    while l1 is not None or l2 is not None:
        if not l1:
            current.next = ListNode(l2.val)
            l2 = l2.next
        elif not l2:
            current.next = ListNode(l1.val)
            l1 = l1.next
        else:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
        
        if head is None:
            head = current
        
        current = current.next
    
    return head
        


def print_list(node: ListNode):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    
    return result
