from data_structures.array.sparse_arrays import matching_strings

def test_matching_strings():
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]

    assert matching_strings(strings, queries) == [2, 1, 0], "Should be [2, 1, 0]"

def test_duplicated_values():
    strings = ["abcde", "sdaklfj", "asdjf", "na", "basdn", "sdaklfj", "asdjf", "na", "asdjf", "na", "basdn", "sdaklfj", "asdjf"]
    queries = ["abcde", "sdaklfj", "asdjf", "na", "basdn"]

    assert matching_strings(strings, queries) == [1, 3, 4, 3, 2], "Should be [1, 3, 4, 3, 2]"
