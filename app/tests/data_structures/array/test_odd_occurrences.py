from data_structures.array.odd_occurrences import find_unpaired_element

def test_find_unpaired_element():
    assert find_unpaired_element([1, 2, 3, 3, 2]) == 1, "[1, 2, 3, 3, 2] should return 1"
    assert find_unpaired_element([1, 2, 3, 3, 2, 1]) == None, "[1, 2, 3, 3, 2, 1] should return None"
    assert find_unpaired_element([1, 2, 1, 5, 4, 5, 2]) == 4, "[1, 2, 1, 5, 4, 5, 2] should return 4"

def test_find_third_unpaired_element():
    assert find_unpaired_element([1, 2, 3, 3, 1, 3, 2]) == 3, "[1, 2, 3, 3, 1, 3, 2] should return 3"