from data_structures.array.right_rotation import rotate

def test_right_rotation():
    assert rotate([1, 2, 3, 4], 1) == [4, 1, 2, 3], "Should be [4, 1, 2, 3]"