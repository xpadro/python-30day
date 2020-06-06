from algorithms.other.a_very_big_sum import a_very_big_sum

def test_sum():
    assert a_very_big_sum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]) == 5000000015, "Should be 5000000015"