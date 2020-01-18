from other_problems.easy.diagonal_difference import diagonalDifference

def test_diagonal_difference():
    assert diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]) == 2, "Should be 2"

def test_diagonal_difference_with_negatives():
    assert diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15, "Should be 15"