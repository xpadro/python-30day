from algorithms.other.valid_anagram import is_valid

def test_is_valid():
    assert is_valid('badcsea', 'ererwna') == False
    assert is_valid('anagram', 'nagaram') == True
    assert is_valid('rat', 'car') == False
    assert is_valid('€a€', 'a€€') == True
    assert is_valid('€a$', 'a€$') == True
    assert is_valid('€a$', 'a€€') == False
