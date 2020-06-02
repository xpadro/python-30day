from algorithms.recursion.fibonacci import find_recursive, find_iterative

def test_fibonacci_recursive():
    assert find_recursive(4) == 3, "fibonacci(4) should return 3"
    assert find_recursive(6) == 8, "fibonacci(6) should return 8"
    assert find_recursive(8) == 21, "fibonacci(8) should return 21"

def test_fibonacci_iterative():
    assert find_iterative(4) == 3, "fibonacci(4) should return 3"
    assert find_iterative(6) == 8, "fibonacci(6) should return 8"
    assert find_iterative(8) == 21, "fibonacci(8) should return 21"