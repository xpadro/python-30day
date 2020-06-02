from algorithms.sorting.selection_sort import sort

def test_sort():
    assert sort([1]) == [1]
    assert sort([2, 1]) == [1, 2]
    assert sort([3, 5, 1, 15, 4, 7, 2]) == [1, 2, 3, 4, 5, 7, 15]