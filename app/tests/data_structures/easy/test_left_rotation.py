from data_structures.easy.left_rotation import rotate

def test_left_rotation():
    assert rotate([1, 2, 3, 4], 2) == [3, 4, 1, 2], "Should be [3, 4, 1, 2]"