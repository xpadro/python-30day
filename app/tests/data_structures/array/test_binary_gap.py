from data_structures.array.binary_gap import binary_gap

def test_binary_gap():
    assert binary_gap(9) == 2, "binary_gap(9) should be 2"
    assert binary_gap(529) == 4, "binary_gap(529) should be 4"
    assert binary_gap(20) == 1, "binary_gap(20) should be 1"
    assert binary_gap(15) == 0, "binary_gap(15) should be 0"
    assert binary_gap(32) == 0, "binary_gap(32) should be 0"