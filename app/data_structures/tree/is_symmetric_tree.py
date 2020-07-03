class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def is_symmetric(root: TreeNode) -> bool:
    if root is None:
        return True
    elif root.left is None and root.right is not None:
        return False
    elif root.left is not None and root.right is None:
        return False

    
    result_left = __search_left_tree(root.left, [])
    result_right = __search_right_tree(root.right, [])
    
    return result_left == result_right
    

def __search_left_tree(node, result):
    if node is not None:
        result.append(node.val)

        result = __search_left_tree(node.left, result)
        result = __search_left_tree(node.right, result)
    else:
        result.append(None)

    return result

def __search_right_tree(node, result):
    if node is not None:
        result.append(node.val)
        result = __search_right_tree(node.right, result)
        result = __search_right_tree(node.left, result)
    else:
        result.append(None)

    return result