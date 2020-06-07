def find_depth(head):
    """ Finds the depth of a binary tree
    
    """

    return __do_find_depth(head, 0)

def __do_find_depth(node, depth):
    depth_left = depth
    depth_right = depth

    if node is not None:
            depth_left = __do_find_depth(node.left, depth + 1)
            depth_right = __do_find_depth(node.right, depth + 1)

    return max(depth_left, depth_right)