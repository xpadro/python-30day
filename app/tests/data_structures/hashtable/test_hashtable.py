from data_structures.hashtable.hashtable import HashTable

def test_hashtable():
    table = HashTable(50)
    table.set('a', 1)

    assert table.get('a') == 1, "Should be 1"

def test_hashtable_override_key():
    table = HashTable(50)
    table.set('a', 1)
    table.set('a', 2)

    assert table.get('a') == 2, "Should be 2"

def test_hashtable_unexisting_key():
    table = HashTable(50)
    table.set('a', 1)

    assert table.get('b') == None, "Should be None"