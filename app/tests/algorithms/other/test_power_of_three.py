from algorithms.other.power_of_three import is_power_of_three

def test_is_power_of_three():
    assert is_power_of_three(0) == False
    assert is_power_of_three(1) == True
    assert is_power_of_three(2) == False
    assert is_power_of_three(3) == True
    assert is_power_of_three(-3) == False
    assert is_power_of_three(27) == True
    assert is_power_of_three(9) == True
    assert is_power_of_three(45) == False
    assert is_power_of_three(81) == True