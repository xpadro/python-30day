from algorithms.other.happy_number import is_happy

def test_is_happy():
    assert is_happy(0) == False
    assert is_happy(1) == True
    assert is_happy(2) == False
    assert is_happy(19) == True
    assert is_happy(12) == False
    assert is_happy(99) == False
    assert is_happy(68) == True
    assert is_happy(100) == True
    assert is_happy(123456) == True
    