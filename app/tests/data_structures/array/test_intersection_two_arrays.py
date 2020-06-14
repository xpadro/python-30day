from data_structures.array.intersection_two_arrays import find_intersection

def test_find():
    assert find_intersection([1,2,2,1], [2,2]) == [2,2]
    assert find_intersection([4,9,5], [9,4,9,8,4]) == [4,9]
    assert find_intersection([1,2,2,3,2,2,1], [2,2,1]) == [1,2,2]
    assert find_intersection([1,2,3], [1]) == [1]
    assert find_intersection([1], [1,2,3]) == [1]
    assert find_intersection([], [1,2,3]) == []
    assert find_intersection([1,2,3], []) == []
    assert find_intersection([4,1,2,2,1], [1,2,3,4]) == [4,1,2]
    assert find_intersection([4,1,2,2,3,1], [1,2,3,4]) == [4,1,2,3]
    assert find_intersection([4,5,2,5,3,5,1,5], [1,2,3,4]) == [4,2,3,1]
    assert find_intersection([1,2], [1,1]) == [1]