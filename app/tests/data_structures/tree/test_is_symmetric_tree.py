from data_structures.tree.is_symmetric_tree import is_symmetric, TreeNode

def test_is_symmetric():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    assert is_symmetric(root) == True


def test_is_not_symmetric():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    assert is_symmetric(root) == False

def test_is_symmetric_with_nones():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    assert is_symmetric(root) == True

def test_none_tree():
    assert is_symmetric(None) == True

def test_only_root_node():
    assert is_symmetric(TreeNode(1)) == True