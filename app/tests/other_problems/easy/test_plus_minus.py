from other_problems.easy.plus_minus import plusMinus

def test_plus_minus():
    assert plusMinus([1, 1, 0, -1, -1]) == [0.4, 0.4, 0.2], "Should be [0.4, 0.4, 0.2]"