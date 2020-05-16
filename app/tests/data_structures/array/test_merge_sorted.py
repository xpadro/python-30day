from data_structures.array.merge_sorted import merge_sorted

def test_merge_sorted():
    assert merge_sorted([1, 2, 5, 8], [3, 4, 7]) == [1, 2, 3, 4, 5, 7, 8], "Should be [1, 2, 3, 4, 5, 7, 8]"

def test_merge_sorted_equal_numbers():
    assert merge_sorted([1, 2, 5], [1, 2, 7]) == [1, 1, 2, 2, 5, 7], "Should be [1, 1, 2, 2, 5, 7]"

def test_merge_sorted_first_empty_array():
    assert merge_sorted([], [1, 2, 7]) == [1, 2, 7], "Should be [1, 2, 7]"

def test_merge_sorted_second_empty_array():
    assert merge_sorted([1, 2, 7], []) == [1, 2, 7], "Should be [1, 2, 7]"