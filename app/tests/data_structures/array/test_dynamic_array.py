from data_structures.array.dynamic_array import dynamic_array

def test_dynamic_array():
    assert dynamic_array(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]) == [7, 3], "Should be [7, 3]"
