from algorithms.other.roman_to_int import to_int

def test_to_int():
    assert to_int("I") == 1
    assert to_int("II") == 2
    assert to_int("III") == 3
    assert to_int("IV") == 4
    assert to_int("IX") == 9
    assert to_int("X") == 10
    assert to_int("XI") == 11
    assert to_int("XII") == 12
    assert to_int("XV") == 15
    assert to_int("CC") == 200
    assert to_int("MM") == 2000
    assert to_int("MCM") == 1900
    assert to_int("MCMLV") == 1955
    assert to_int("MCMLIV") == 1954
    