from data_structures.array.majority_element import find_majority

def test_find_majority():
    assert find_majority([3, 2, 3]) == 3
    assert find_majority([2,2,1,1,1,2,2]) == 2