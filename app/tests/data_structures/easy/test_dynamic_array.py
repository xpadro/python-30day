from data_structures.easy.dynamic_array import dynamicArray

def test_dynamic_array():
    assert dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]) == [7, 3], "Should be [7, 3]"
