from algorithms.other.climbing_stairs import find_solutions

def test_climb():
    assert find_solutions(1) == 1
    assert find_solutions(2) == 2
    assert find_solutions(3) == 3
    assert find_solutions(4) == 5
    assert find_solutions(5) == 8
    assert find_solutions(10) == 89
