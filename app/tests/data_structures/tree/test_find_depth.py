from data_structures.tree.binary_search_tree import BinarySearchTree, Node
from data_structures.tree.find_depth import find_depth

def test_find_depth():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(8)
    tree.insert(12)
    tree.insert(4)
    tree.insert(9)

    assert find_depth(tree.root) == 3
