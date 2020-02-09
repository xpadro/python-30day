from data_structures.medium.sparse_arrays import matchingStrings

def test_matchingStrings():
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]

    assert matchingStrings(strings, queries) == [2, 1, 0], "Should be [2, 1, 0]"

def test_duplicated_values():
    strings = ["abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"]
    queries = ["abcde", "sdaklfj", "asdjf", "na", "basdn"]

    assert matchingStrings(strings, queries) == [1, 3, 4, 3, 2], "Should be [1, 3, 4, 3, 2]"
