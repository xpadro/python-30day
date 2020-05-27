from data_structures.hashtable.first_recurring_char import first_recurring_char

def test_first_recurring_char_1():
    assert first_recurring_char([2, 5, 1, 2, 3, 5, 1, 2, 4]) == 2, "Should be 2"

def test_first_recurring_char_2():
    assert first_recurring_char([2, 1, 1, 2, 3, 5, 1, 2, 4]) == 1, "Should be 1"

def test_first_recurring_char_not_found():
    assert first_recurring_char([2, 3, 4, 5]) == None, "Should be None"