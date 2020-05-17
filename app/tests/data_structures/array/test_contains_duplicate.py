from data_structures.array.contains_duplicate import contains_duplicate

def test_contains_duplicate():
    assert contains_duplicate([1,2,3,1]) == True, "Should be True"

def test_does_not_contain_duplicate():
    assert contains_duplicate([1,2,3,4]) == False, "Should be False"