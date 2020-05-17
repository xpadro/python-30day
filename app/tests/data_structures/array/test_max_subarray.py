from data_structures.array.max_subarray import max_subarray

def test_two_sum():
    assert max_subarray([-2,1,-3,4,-1,2,1,-5,4]) == 6, "Should be 6"