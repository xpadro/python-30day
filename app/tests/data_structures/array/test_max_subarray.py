from data_structures.array.max_subarray import max_subarray

def test_two_sum():
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6, "Should be 6"
    assert max_subarray([1]) == 1
    assert max_subarray([-1]) == -1
    assert max_subarray([0]) == 0
    assert max_subarray(None) == 0
    assert max_subarray([-1, 4, 2, -5, 5, 2]) == 8
    assert max_subarray([-1,1,-2,1,1]) == 2
    assert max_subarray([-2,-1]) == -1