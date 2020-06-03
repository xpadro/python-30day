from data_structures.tree.binary_search_tree import BinarySearchTree, Node

def test_binary_tree_insert():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(12)
    tree.insert(4)
    tree.insert(9)

    assert tree.root.value == 10, "root should be 10"

    # left subtree
    assert tree.root.left.value == 8, "root should be 8"
    assert tree.root.left.left.value == 4, "root should be 4"
    assert tree.root.left.right.value == 9, "root should be 9"

    # right subtree
    assert tree.root.right.value == 12, "root should be 12"

def test_binary_tree_lookup():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(12)
    tree.insert(4)
    tree.insert(9)

    assert tree.lookup(10) == 10, "Should have found 10"
    assert tree.lookup(8) == 8, "Should have found 8"
    assert tree.lookup(4) == 4, "Should have found 4"
    assert tree.lookup(15) == None, "Should have not found the value"

def test_bfs():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(12)
    tree.insert(4)
    tree.insert(9)

    assert tree.bfs() == [10, 8, 12, 4, 9]

def test_dfs():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(12)
    tree.insert(4)
    tree.insert(9)

    assert tree.dfs() == [10, 8, 4, 9, 12]

