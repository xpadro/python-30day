from data_structures.hard.array_manipulation import arrayManipulation

def test_arrayManipulation_usecase_1():
    assert arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]) == 200, "Should be 200"

def test_arrayManipulation_usecase_2():
    assert arrayManipulation(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]) == 31, "Should be 31"
