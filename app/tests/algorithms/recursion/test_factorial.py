from algorithms.recursion.factorial import find_recursive, find_iterative

def test_factorial_recursive():
    assert find_recursive(4) == 24, "factorial(4) should return 24"
    assert find_recursive(1) == 1, "factorial(1) should return 1"

def test_factorial_iterative():
    assert find_iterative(4) == 24, "factorial(4) should return 24"
    assert find_iterative(1) == 1, "factorial(1) should return 1"