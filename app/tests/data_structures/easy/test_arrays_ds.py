from data_structures.easy.arrays_ds import reverseArray

def test_reverse_array():
    assert reverseArray([3, 1, 4 ,2]) == "2 4 1 3", "Should be 2 4 1 3"

def test_reverse_array_bigger_numbers():
    assert reverseArray([6676, 3216, 4063, 8373, 423, 586, 8850, 6762]) == "6762 8850 586 423 8373 4063 3216 6676", "Should be 6762 8850 586 423 8373 4063 3216 6676"
