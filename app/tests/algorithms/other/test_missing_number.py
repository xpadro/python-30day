from algorithms.other.missing_number import find

def test_find():
    assert find([3,0,1]) == 2
    assert find([9,6,4,2,3,5,7,0,1]) == 8
    assert find([1]) == 0
    assert find([]) == 0
    assert find([1, 2, 3]) == 0
