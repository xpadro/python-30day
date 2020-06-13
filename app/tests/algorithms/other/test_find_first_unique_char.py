from algorithms.other.find_first_unique_char import find

def test_find_unique():
    assert find("l") == 0
    assert find("lal") == 1
    assert find("llla") == 3
    assert find("leetcode") == 0
    assert find("loveleetcode") == 2
    assert find("lllaa") == -1
