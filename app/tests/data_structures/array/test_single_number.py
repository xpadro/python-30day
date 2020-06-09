from data_structures.array.single_number import find_single

def test_find_single():
    assert find_single([3, 2, 3]) == 2
    assert find_single([2,2,1,1,3]) == 3
    assert find_single([4,1,2,1,2]) == 4