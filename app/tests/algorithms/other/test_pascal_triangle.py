from algorithms.other.pascal_triangle import pascal_triangle

def test_pascal_triangle():
    assert pascal_triangle(0) == []
    assert pascal_triangle(1) == [[1]]
    assert pascal_triangle(2) == [[1], [1, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]