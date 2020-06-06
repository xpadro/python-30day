from data_structures.array.reverse_array_inplace import reverse

def test_reverse_array():
    assert reverse([3, 1, 4 ,2]) == [2, 4, 1, 3], "Should be [2, 4, 1, 3]"

