from algorithms.other.plus_minus import plus_minus

def test_plus_minus():
    assert plus_minus([1, 1, 0, -1, -1]) == [0.4, 0.4, 0.2], "Should be [0.4, 0.4, 0.2]"